### Alejandro Friant 2025
### Version 8.4

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

    title = "User and Depot Management"
    user_win.addstr(1, (win_w - len(title)) // 2, title)

    text_lines = [
        "User management is done with P4Admin from your computer.",
        "",
        "Recommended steps:",
        "1. Download the 'Helix Visual Client' (P4V) from Perforce.com.",
        "   This package includes the P4V and P4Admin tools.",
        "",
        "2. Open P4Admin and connect to your server:",
        "   - Server: Your Raspberry Pi's IP (e.g., 192.168.100.35:1666)",
        "   - User: admin     - Password: admin12345",
        "   - This password should be changed on the first connection.",
        "",
        "4. In P4V, create your first depot. A 'stream' type is recommended.",
        "   Example name: 'streamMyproject'",
        "",
        "5. P4V is used for daily work with files (streams/workspaces).",
        "   P4Admin is used only to manage users, depots, and permissions."
    ]

    y_pos = 3
    for line in text_lines:
        user_win.addstr(y_pos, 3, line)
        y_pos += 1

    user_win.addstr(win_h - 2, (win_w - len("Press Esc to return")) // 2, "Press Esc to return")
    user_win.refresh()

    while True:
        key = user_win.getch()
        if key == 27: # ESC
            break