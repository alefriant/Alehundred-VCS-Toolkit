### Alejandro Friant 2025
### Version 9.2

from . import tui
import curses

def start_app(stdscr):
    try:
        app_tui = tui.TUIController(stdscr)
        app_tui.run()
    except curses.error as e:
        curses.endwin()
        print(f"Curses Error: A larger terminal is required.")
        print(f"Detail: {e}")
    except KeyboardInterrupt:
        pass

def main():
    try:
        curses.wrapper(start_app)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
    main()