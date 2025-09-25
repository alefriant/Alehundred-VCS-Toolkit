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

    title = "Restart Server Instructions"
    restart_win.addstr(1, (win_w - len(title)) // 2, title)

    y_pos = 5
    
    restart_win.addstr(y_pos, 3, "If the Perforce server is not running (e.g., after a system reboot),")
    restart_win.addstr(y_pos + 1, 3, "run the following command in the terminal to start it manually:")
    
    command = "sudo /usr/local/bin/p4d -r /opt/perforce/servers/master -p 1666 -d"
    restart_win.addstr(y_pos + 4, (win_w - len(command)) // 2, command, curses.A_BOLD)

    restart_win.addstr(y_pos + 7, 3, "To copy, select the text in the terminal with your PC's mouse.")

    restart_win.addstr(win_h - 2, (win_w - len("Press Esc to return")) // 2, "Press Esc to return")
    restart_win.refresh()

    while True:
        key = restart_win.getch()
        if key == 27: # ESC
            break