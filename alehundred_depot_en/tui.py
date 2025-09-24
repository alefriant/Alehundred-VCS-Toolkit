### Alejandro Friant 2025
### Version 8.0

import time
import curses
from . import p4_manager
from . import tui_help
from . import tui_status
from . import tui_user

class TUIController:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.p4_manager = p4_manager.P4Manager()
        
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN)
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
        
        self.color_main_win = curses.color_pair(1)
        self.color_cyan_text = curses.color_pair(2)
        self.color_yellow_text = curses.color_pair(3)
        self.color_panel_win = curses.color_pair(4)
        self.color_dialog_win = curses.color_pair(5)

    def _get_centered_coords(self, win_h, win_w):
        term_h, term_w = self.stdscr.getmaxyx()
        y = (term_h - win_h) // 2
        x = (term_w - win_w) // 2
        return y, x

    def _draw_main_window(self):
        self.stdscr.clear()
        win_h, win_w = 24, 80
        win_y, win_x = self._get_centered_coords(win_h, win_w)

        window = curses.newwin(win_h, win_w, win_y, win_x)
        window.bkgd(' ', self.color_main_win)
        window.keypad(True)
        window.box()
        
        title = "Alehundred-Depot"
        window.addstr(1, (win_w - len(title)) // 2, title)
        
        menu_lines = [
            "1. Install Perforce Server (MVP)",
            "2. Manage Users",
            "3. View Server Status",
            "4. Exit"
        ]
        for i, line in enumerate(menu_lines):
            num, text = line.split('.', 1)
            window.addstr(6 + (i * 3), (win_w - len(line)) // 2, num + ".", self.color_cyan_text)
            window.addstr(text, self.color_main_win)
            
        footer_key = {'x': 3, 'key': 'F1', 'text': ' Help'}
        window.addstr(win_h - 2, footer_key['x'], footer_key['key'], self.color_yellow_text)
        window.addstr(footer_key['text'], self.color_main_win)

        version_str = "Alehundred-Depot 8.0"
        window.addstr(win_h - 2, win_w - len(version_str) - 2, version_str)
        
        self.stdscr.refresh()
        window.refresh()
        return window

    def _show_dialog(self, title, message_lines, wait_for_esc=True):
        flat_lines = []
        for line in message_lines:
            flat_lines.extend(line.split('\n'))

        if wait_for_esc:
            flat_lines.append("")
            flat_lines.append("Press Esc to exit")

        msg_w = max(len(line) for line in flat_lines) + 4
        win_h, win_w = len(flat_lines) + 4, msg_w
        win_y, win_x = self._get_centered_coords(win_h, win_w)
        
        dialog = curses.newwin(win_h, win_w, win_y, win_x)
        dialog.bkgd(' ', self.color_dialog_win)
        dialog.keypad(True)
        dialog.box()
        dialog.addstr(1, (win_w - len(title)) // 2, title)

        for i, line in enumerate(flat_lines):
            dialog.addstr(2 + i, (win_w - len(line)) // 2, line)
        
        dialog.refresh()
        
        if wait_for_esc:
            while True:
                key = dialog.getch()
                if key == 27: # ESC
                    break
        return dialog

    def _show_confirmation(self):
        dialog = self._show_dialog("Confirm", ["Do you want to exit? (Y/N)"], wait_for_esc=False)
        while True:
            key = dialog.getkey().lower()
            if key in ['y', 'n']:
                del dialog
                return key == 'y'

    def _show_scrolling_log(self, title, generator_func):
        win_h, win_w = 22, 78
        win_y, win_x = self._get_centered_coords(win_h, win_w)
        
        log_win = curses.newwin(win_h, win_w, win_y, win_x)
        log_win.bkgd(' ', self.color_panel_win)
        log_win.keypad(True)
        log_win.box()
        log_win.addstr(0, 2, f" {title} (Generating real-time log...) ")
        log_win.refresh()

        pad_h, pad_w = 1000, win_w - 2
        pad = curses.newpad(pad_h, pad_w)
        pad.bkgd(' ', self.color_panel_win)
        
        lines = []
        final_status = None
        final_message = ""
        last_progress_bucket = -1

        log_generator = generator_func()
        for status, data in log_generator:
            needs_redraw = False
            
            if status == 'ALREADY_INSTALLED':
                final_status = 'ALREADY_INSTALLED'
                break
            elif status == 'ERROR':
                final_status = 'ERROR'
                final_message = data
                lines.append(f"ERROR: {data}")
                needs_redraw = True
                break
            elif status == 'SUCCESS':
                final_status = 'SUCCESS'
                final_message = data
                break 
            elif status == 'PROGRESS':
                current_bucket = int(data / 10)
                if current_bucket > last_progress_bucket:
                    last_progress_bucket = current_bucket
                    progress_bar = '█' * int(data / 4) + '─' * (25 - int(data / 4))
                    lines[-1] = f"   -> [{progress_bar}] {data:.1f}%"
                    needs_redraw = True
            else: 
                lines.append(data)
                needs_redraw = True
                if "Downloading" in data:
                    last_progress_bucket = -1
            
            if needs_redraw:
                pad.clear()
                for i, line in enumerate(lines):
                    if i < pad_h: pad.addstr(i, 0, line)
                
                scroll_pos = max(0, len(lines) - (win_h - 2))
                pad.refresh(scroll_pos, 0, win_y + 1, win_x + 1, win_y + win_h - 2, win_x + win_w - 2)
        
        if final_status != 'ALREADY_INSTALLED':
            lines.append("--- Process Finished ---")
            lines.append("")
            lines.append("Press Esc to see the final summary...")
            pad.clear()
            for i, line in enumerate(lines):
                if i < pad_h: pad.addstr(i, 0, line)
            
            log_win.addstr(0, 2, f" {title} (Use arrows, Esc to exit) ")
            log_win.refresh()
            scroll_pos = max(0, len(lines) - (win_h - 2))
            pad.refresh(scroll_pos, 0, win_y + 1, win_x + 1, win_y + win_h - 2, win_x + win_w - 2)

            while True:
                key = log_win.getch()
                if key == curses.KEY_UP and scroll_pos > 0:
                    scroll_pos -= 1
                elif key == curses.KEY_DOWN and scroll_pos < len(lines) - (win_h - 2):
                    scroll_pos += 1
                elif key == 27:
                    break
                pad.refresh(scroll_pos, 0, win_y + 1, win_x + 1, win_y + win_h - 2, win_x + win_w - 2)

        if final_status == 'SUCCESS':
            self._show_dialog("Success", [final_message])
        elif final_status == 'ERROR':
            self._show_dialog("Error", [final_message])
        elif final_status == 'ALREADY_INSTALLED':
            self._show_dialog("Information", ["The server is already installed."])

    def run(self):
        while True:
            main_window = self._draw_main_window()
            key = main_window.getch()

            key_char = ""
            if isinstance(key, int) and 32 <= key <= 126:
                key_char = chr(key)
            
            if key_char == '1':
                self._show_scrolling_log("Installation Log", self.p4_manager.instalar_servidor)

            elif key_char == '2':
                tui_user.show_user_screen(self.stdscr)
            
            elif key_char == '3':
                tui_status.show_status_screen(self.stdscr, self.p4_manager)

            elif key == curses.KEY_F1:
                tui_help.show_help_screen(self.stdscr)

            elif key_char == '4':
                if self._show_confirmation():
                    break