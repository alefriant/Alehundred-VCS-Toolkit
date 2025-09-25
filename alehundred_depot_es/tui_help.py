### Alejandro Friant 2025
### Version 9.2

import curses

def show_help_screen(stdscr):
    term_h, term_w = stdscr.getmaxyx()
    win_h, win_w = 22, 78
    win_y = (term_h - win_h) // 2
    win_x = (term_w - win_w) // 2

    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN)
    color_panel = curses.color_pair(4)

    help_win = curses.newwin(win_h, win_w, win_y, win_x)
    help_win.bkgd(' ', color_panel)
    help_win.keypad(True)
    help_win.box()

    title = "Ayuda e Información Importante"
    help_win.addstr(1, (win_w - len(title)) // 2, title)

    y_pos = 3
    
    help_win.addstr(y_pos, 3, "--- Superusuario por Defecto ---")
    help_win.addstr(y_pos + 1, 3, "- Usuario: admin     - Contraseña: admin12345")
    help_win.addstr(y_pos + 2, 3, "- Se recomienda cambiar esta contraseña en la primera conexión.")
    y_pos += 4

    help_win.addstr(y_pos, 3, "--- Desinstalación (Bajo su responsabilidad) ---")
    help_win.addstr(y_pos + 1, 3, "ADVERTENCIA: El siguiente comando eliminará TODOS los datos.")
    help_win.addstr(y_pos + 2, 3, "sudo pkill p4d; sudo rm -f /usr/local/bin/p4*; sudo rm -rf /opt/perforce")
    help_win.addstr(y_pos + 3, 3, "Para copiar, seleccione el texto con el ratón de su PC en la terminal.")
    y_pos += 5

    help_win.addstr(y_pos, 3, "--- Apoya a Perforce ---")
    help_win.addstr(y_pos + 1, 3, "Si necesita más de 5 usuarios o 20 workspaces, Perforce ofrece licencias")
    help_win.addstr(y_pos + 2, 3, "y servicios en la nube con Helix Core Cloud.")
    y_pos += 4
    
    help_win.addstr(y_pos, 3, "--- Seguridad SSL ---")
    help_win.addstr(y_pos + 1, 3, "SSL desactivado por defecto para simplificar la red local.")

    help_win.addstr(win_h - 2, (win_w - len("Presione Esc para volver")) // 2, "Presione Esc para volver")
    help_win.refresh()

    while True:
        key = help_win.getch()
        if key == 27: # ESC
            break