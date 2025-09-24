### Alejandro Friant 2025
### Version 8.0

import subprocess
import os
import requests
import sys
import re

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BG_BLUE = '\033[44m'

def ejecutar_comando_sistema(comando: list, con_sudo: bool = False):
    try:
        if con_sudo:
            comando.insert(0, 'sudo')
        resultado = subprocess.run(comando, capture_output=True, text=True, check=False)
        return (resultado.returncode, resultado.stdout, resultado.stderr)
    except Exception as e:
        return (1, "", f"Unexpected error: {e}")

def get_disk_usage():
    code, out, _ = ejecutar_comando_sistema(["df", "-h", "/"])
    if code == 0:
        lines = out.strip().split('\n')
        if len(lines) > 1:
            parts = lines[1].split()
            return f"{parts[2]} / {parts[1]} ({parts[4]} Used)"
    return "Not available"

def get_mem_usage():
    code, out, _ = ejecutar_comando_sistema(["free", "-m"])
    if code == 0:
        lines = out.strip().split('\n')
        if len(lines) > 1:
            parts = lines[1].split()
            return f"{parts[2]}MB / {parts[1]}MB Used"
    return "Not available"

def get_cpu_usage():
    code, out, _ = ejecutar_comando_sistema(["top", "-bn1"])
    if code == 0:
        match = re.search(r"Cpu\(s\):\s+([\d.]+)%? us", out)
        if match:
            return f"{match.group(1)}% (User)"
    return "Not available"

def limpiar_pantalla():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def ejecutar_y_yield_salida(comando: list, con_sudo: bool = False):
    try:
        if con_sudo:
            comando.insert(0, 'sudo')
        
        process = subprocess.Popen(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        for line in iter(process.stdout.readline, ''):
            yield ('LOG', line.strip())
        
        process.stdout.close()
        return_code = process.wait()
        yield ('RETURN_CODE', return_code)

    except Exception as e:
        yield ('LOG', f"Unexpected error executing command: {e}")
        yield ('RETURN_CODE', 1)


def descargar_con_progreso(url: str, destino: str):
    try:
        dir_destino = os.path.dirname(destino)
        ejecutar_comando_sistema(["mkdir", "-p", dir_destino], con_sudo=True)
        ejecutar_comando_sistema(["touch", destino], con_sudo=True)
        ejecutar_comando_sistema(["chmod", "666", destino], con_sudo=True)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            block_size = 8192
            
            with open(destino, 'wb') as f:
                descargado = 0
                for chunk in r.iter_content(chunk_size=block_size):
                    f.write(chunk)
                    descargado += len(chunk)
                    if total_size > 0:
                        porcentaje = (descargado / total_size) * 100
                        yield ('PROGRESS', porcentaje)
        
        return (0, "")

    except Exception as e:
        return (1, str(e))