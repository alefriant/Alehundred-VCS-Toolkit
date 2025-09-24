### Alejandro Friant 2025
### Version 8.0

import curses

def show_status_screen(stdscr, p4_manager):
    term_h, term_w = stdscr.getmaxyx()
    win_h, win_w = 22, 78
    win_y = (term_h - win_h) // 2
    win_x = (term_w - win_w) // 2

    # Color para la ventana de panel
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN)
    color_panel = curses.color_pair(4)

    status_win = curses.newwin(win_h, win_w, win_y, win_x)
    status_win.bkgd(' ', color_panel)
    status_win.keypad(True)
    status_win.box()

    title = "Estado del Servidor y Sistema"
    status_win.addstr(1, (win_w - len(title)) // 2, title)
    status_win.addstr(3, (win_w - len("Consultando...")) // 2, "Consultando...")
    status_win.refresh()
    
    status_data = p4_manager.get_server_status()

    status_win.clear()
    status_win.bkgd(' ', color_panel)
    status_win.box()
    status_win.addstr(1, (win_w - len(title)) // 2, title)

    y_pos = 3
    for section, data in status_data.items():
        status_win.addstr(y_pos, 3, f"--- {section} ---", curses.A_BOLD)
        y_pos += 1
        for key, value in data.items():
            status_win.addstr(y_pos, 5, f"{key}: {value}")
            y_pos += 1
        y_pos += 1

    status_win.addstr(win_h - 2, (win_w - len("Presione Esc para volver")) // 2, "Presione Esc para volver")
    status_win.refresh()

    while True:
        key = status_win.getch()
        if key == 27: # ESC
            break