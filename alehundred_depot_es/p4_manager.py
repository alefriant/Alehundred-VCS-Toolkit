### Alejandro Friant 2025
### Version 9.2

from . import utils
import time
import subprocess
import os

class P4Manager:
    def get_server_status(self):
        status_info = {
            "Estado Servidor Perforce": {
                "Estado": "Detenido",
                "Detalles": "No se pudo obtener información."
            },
            "Recursos del Sistema": {
                "Uso de CPU": utils.get_cpu_usage(),
                "Uso de Memoria": utils.get_mem_usage(),
                "Uso de Disco (/)": utils.get_disk_usage(),
                "Temperatura CPU": utils.get_cpu_temp()
            }
        }
        
        INSTALL_PATH_P4_CLIENT = "/usr/local/bin/p4"
        P4_PORT = "1666"
        
        code, out, _ = utils.ejecutar_comando_sistema(["pgrep", "p4d"])
        if code == 0:
            status_info["Estado Servidor Perforce"]["Estado"] = "En Ejecución"
            
            code_info, out_info, err_info = utils.ejecutar_comando_sistema([INSTALL_PATH_P4_CLIENT, "-p", P4_PORT, "info"])
            if code_info == 0:
                status_info["Estado Servidor Perforce"]["Detalles"] = "Respondiendo OK."
                
                info_dict = {}
                for line in out_info.strip().split('\n'):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        key, value = parts
                        info_dict[key.strip()] = value.strip()
                
                status_info["Información de P4D"] = {
                    "Server address": info_dict.get("Server address", "N/A"),
                    "Server uptime": info_dict.get("Server uptime", "N/A"),
                    "Server version": info_dict.get("Server version", "N/A"),
                }
            else:
                status_info["Estado Servidor Perforce"]["Detalles"] = f"Proceso activo, pero no responde en el puerto {P4_PORT}."
        
        return status_info

    def instalar_servidor(self):
        P4D_URL = "https://filehost.perforce.com/perforce/r25.1/bin.linux26aarch64/p4d"
        P4_CLIENT_URL = "https://filehost.perforce.com/perforce/r25.1/bin.linux26aarch64/p4"
        
        INSTALL_PATH_P4D = "/usr/local/bin/p4d"
        INSTALL_PATH_P4_CLIENT = "/usr/local/bin/p4"
        
        P4_ROOT = "/opt/perforce/servers/master"
        P4_PORT = "1666"

        if os.path.exists(INSTALL_PATH_P4D):
            yield ('ALREADY_INSTALLED', None)
            return

        steps = [
            ("Paso 1: Actualizando lista de paquetes...", ["apt-get", "update"], True),
            ("Paso 2: Instalando dependencias...", ["apt-get", "install", "-y", "wget", "python3-requests"], True)
        ]

        for desc, cmd, sudo in steps:
            yield ('STATUS', desc)
            final_code = 1
            for status, data in utils.ejecutar_y_yield_salida(cmd, con_sudo=sudo):
                if status == 'RETURN_CODE':
                    final_code = data
                else:
                    yield (status, data)
            
            if final_code != 0:
                yield ('ERROR', f"Falló el paso: {desc}")
                return
            yield ('STATUS', "... OK")

        yield ('STATUS', "Paso 3: Descargando el binario del Servidor (p4d)...")
        downloader = utils.descargar_con_progreso(P4D_URL, INSTALL_PATH_P4D)
        try:
            for status, data in downloader:
                if status == 'PROGRESS':
                    yield (status, data)
        except TypeError:
            code, err = downloader
            if code != 0:
                yield ('ERROR', f"Error en descarga (p4d): {err}")
                return
        yield ('STATUS', "... OK")
        
        yield ('STATUS', "Paso 4: Descargando el binario del Cliente (p4)...")
        downloader = utils.descargar_con_progreso(P4_CLIENT_URL, INSTALL_PATH_P4_CLIENT)
        try:
            for status, data in downloader:
                if status == 'PROGRESS':
                    yield (status, data)
        except TypeError:
            code, err = downloader
            if code != 0:
                yield ('ERROR', f"Error en descarga (p4): {err}")
                return
        yield ('STATUS', "... OK")

        post_download_steps = [
            ("Paso 5: Otorgando permisos de ejecución...", ["chmod", "+x", INSTALL_PATH_P4D, INSTALL_PATH_P4_CLIENT], True),
            (f"Paso 6: Creando directorio raíz en {P4_ROOT}...", ["mkdir", "-p", P4_ROOT], True)
        ]

        for desc, cmd, sudo in post_download_steps:
            yield ('STATUS', desc)
            code, _, stderr = utils.ejecutar_comando_sistema(cmd, con_sudo=sudo)
            if code != 0:
                yield ('ERROR', f"Falló el paso: {desc} -> {stderr.strip()}")
                return
            yield ('STATUS', "... OK")

        yield ('STATUS', f"Paso 7: Iniciando el servidor Perforce...")
        start_cmd = ["sudo", INSTALL_PATH_P4D, "-r", P4_ROOT, "-p", P4_PORT, "-d"]
        subprocess.Popen(start_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        yield ('LOG', "   -> Servidor lanzado, verificando estado...")
        
        server_is_up = False
        for i in range(10):
            time.sleep(1)
            yield ('LOG', f"      Intento de conexión {i+1}/10...")
            check_cmd = [INSTALL_PATH_P4_CLIENT, "-p", P4_PORT, "info"]
            code, _, _ = utils.ejecutar_comando_sistema(check_cmd, con_sudo=False)
            if code == 0:
                server_is_up = True
                break
        
        if not server_is_up:
            yield ('ERROR', "¡El servidor no respondió después de 10 segundos!")
            return
        yield ('STATUS', "... OK")

        yield ('STATUS', "Paso 8: Creando superusuario 'admin'...")
        user_spec = f"User:\tadmin\nEmail:\tadmin@localhost\nFullName:\tAdmin User"
        create_user_cmd = ["sudo", INSTALL_PATH_P4_CLIENT, "-p", P4_PORT, "user", "-f", "-i"]
        
        proc_user = subprocess.run(create_user_cmd, input=user_spec, text=True, capture_output=True)
        if proc_user.returncode != 0:
            yield ('ERROR', f"Falló la creación del superusuario.\nDetalle: {proc_user.stderr.strip()}")
            return

        pass_spec = f"admin12345\nadmin12345"
        set_pass_cmd = ["sudo", INSTALL_PATH_P4_CLIENT, "-p", P4_PORT, "-u", "admin", "passwd"]
        proc_pass = subprocess.run(set_pass_cmd, input=pass_spec, text=True, capture_output=True)
        if proc_pass.returncode != 0:
            yield ('ERROR', f"Falló el establecimiento de la contraseña.\nDetalle: {proc_pass.stderr.strip()}")
            return
        yield ('STATUS', "... OK")

        yield ('SUCCESS', f"Servidor Perforce en ejecución.\n\nSuperusuario 'admin' creado con éxito.")