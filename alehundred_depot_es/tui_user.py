### Alejandro Friant 2025
### Version 9.2

import curses

def show_user_screen(stdscr):
    term_h, term_w = stdscr.getmaxyx()
    win_h, win_w = 22, 78
    win_y = (term_h - win_h) // 2
    win_x = (term_w - win_w) // 2

    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN)
    color_panel = curses.color_pair(4)

    user_win = curses.newwin(win_h, win_w, win_y, win_x)
    user_win.bkgd(' ', color_panel)
    user_win.keypad(True)
    user_win.box()

    title = "Gestión de Usuarios y Depots"
    user_win.addstr(1, (win_w - len(title)) // 2, title)

    text_lines = [
        "La gestión de usuarios se realiza con P4Admin desde su computador.",
        "",
        "Pasos recomendados:",
        "1. Descargue el 'Helix Visual Client' (P4V) desde Perforce.com.",
        "   Este paquete incluye las herramientas P4V y P4Admin.",
        "",
        "2. Abra P4Admin y conéctese a su servidor:",
        "   - Server: La IP de su Raspberry Pi (ej: 192.168.100.35:1666)",
        "   - Usuario: admin     - Contraseña: admin12345",
        "   - Se debe cambiar esta contraseña en la primera conexión.",
        "",
        "4. En P4V, cree su primer depot. Se recomienda del tipo 'stream'.",
        "   Ejemplo de nombre: 'streamMiproyecto'",
        "",
        "5. P4V se usa para el trabajo diario con archivos (streams/workspaces).",
        "   P4Admin se usa solo para administrar usuarios, depots y permisos."
    ]

    y_pos = 3
    for line in text_lines:
        user_win.addstr(y_pos, 3, line)
        y_pos += 1

    user_win.addstr(win_h - 2, (win_w - len("Presione Esc para volver")) // 2, "Presione Esc para volver")
    user_win.refresh()

    while True:
        key = user_win.getch()
        if key == 27: # ESC
            break