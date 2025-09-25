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

    title = "Help and Important Information"
    help_win.addstr(1, (win_w - len(title)) // 2, title)

    y_pos = 3
    
    help_win.addstr(y_pos, 3, "--- Default Superuser ---")
    help_win.addstr(y_pos + 1, 3, "- User: admin     - Password: admin12345")
    help_win.addstr(y_pos + 2, 3, "- It is recommended to change this password on the first connection.")
    y_pos += 4

    help_win.addstr(y_pos, 3, "--- Uninstallation (At your own risk) ---")
    help_win.addstr(y_pos + 1, 3, "WARNING: The following command will delete ALL data.")
    help_win.addstr(y_pos + 2, 3, "sudo pkill p4d; sudo rm -f /usr/local/bin/p4*; sudo rm -rf /opt/perforce")
    help_win.addstr(y_pos + 3, 3, "To copy, select the text in the terminal with your PC's mouse.")
    y_pos += 5

    help_win.addstr(y_pos, 3, "--- Support Perforce ---")
    help_win.addstr(y_pos + 1, 3, "If you need more than 5 users or 20 workspaces, Perforce offers licenses")
    help_win.addstr(y_pos + 2, 3, "and cloud services with Helix Core Cloud.")
    y_pos += 4
    
    help_win.addstr(y_pos, 3, "--- SSL Security ---")
    help_win.addstr(y_pos + 1, 3, "SSL is disabled by default to simplify local networking.")

    help_win.addstr(win_h - 2, (win_w - len("Press Esc to return")) // 2, "Press Esc to return")
    help_win.refresh()

    while True:
        key = help_win.getch()
        if key == 27: # ESC
            break