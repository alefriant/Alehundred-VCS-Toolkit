### Alejandro Friant 2025
### Version 9.2

import curses
import time

def show_status_screen(stdscr, p4_manager):
    term_h, term_w = stdscr.getmaxyx()
    win_h, win_w = 22, 78
    win_y = (term_h - win_h) // 2
    win_x = (term_w - win_w) // 2

    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN)
    color_panel = curses.color_pair(4)

    status_win = curses.newwin(win_h, win_w, win_y, win_x)
    status_win.bkgd(' ', color_panel)
    status_win.keypad(True)
    status_win.box()

    title = "Estado del Servidor y Sistema (Refresco cada 3s)"
    status_win.addstr(1, (win_w - len(title)) // 2, title)
    status_win.addstr(3, (win_w - len("Consultando...")) // 2, "Consultando...")
    status_win.refresh()
    
    status_win.nodelay(True)
    last_update_time = 0

    while True:
        key = status_win.getch()
        if key == 27: # ESC
            break

        current_time = time.time()
        if current_time - last_update_time < 3:
            time.sleep(0.1)
            continue
        
        last_update_time = current_time
        status_data = p4_manager.get_server_status()

        status_win.clear()
        status_win.bkgd(' ', color_panel)
        status_win.box()
        status_win.addstr(1, (win_w - len(title)) // 2, title)

        y_pos = 3
        for section, data in status_data.items():
            status_win.addstr(y_pos, 3, f"--- {section} ---", curses.A_BOLD)
            y_pos += 1
            for data_key, value in data.items():
                line = f"{data_key}: {value}"
                status_win.addstr(y_pos, 5, line.ljust(win_w - 10))
                y_pos += 1
            y_pos += 1

        status_win.addstr(win_h - 2, (win_w - len("Presione Esc para volver")) // 2, "Presione Esc para volver")
        status_win.refresh()