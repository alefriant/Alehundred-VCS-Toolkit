### Alejandro Friant 2025
### Version 9.2

import curses

def show_restart_screen(stdscr):
    term_h, term_w = stdscr.getmaxyx()
    win_h, win_w = 22, 78
    win_y = (term_h - win_h) // 2
    win_x = (term_w - win_w) // 2

    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN)
    color_panel = curses.color_pair(4)

    restart_win = curses.newwin(win_h, win_w, win_y, win_x)
    restart_win.bkgd(' ', color_panel)
    restart_win.keypad(True)
    restart_win.box()

    title = "Instrucciones para Reiniciar el Servidor"
    restart_win.addstr(1, (win_w - len(title)) // 2, title)

    y_pos = 5
    
    restart_win.addstr(y_pos, 3, "Si el servidor Perforce no está en ejecución (ej: tras reiniciar el sistema),")
    restart_win.addstr(y_pos + 1, 3, "ejecute el siguiente comando en la terminal para iniciarlo manualmente:")
    
    command = "sudo /usr/local/bin/p4d -r /opt/perforce/servers/master -p 1666 -d"
    restart_win.addstr(y_pos + 4, (win_w - len(command)) // 2, command, curses.A_BOLD)

    restart_win.addstr(y_pos + 7, 3, "Para copiar, seleccione el texto en la terminal con el ratón de su PC.")

    restart_win.addstr(win_h - 2, (win_w - len("Presione Esc para volver")) // 2, "Presione Esc para volver")
    restart_win.refresh()

    while True:
        key = restart_win.getch()
        if key == 27: # ESC
            break