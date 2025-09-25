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
        print(f"Error de Curses: Se necesita una terminal más grande.")
        print(f"Detalle: {e}")
    except KeyboardInterrupt:
        pass

def main():
    try:
        curses.wrapper(start_app)
    except KeyboardInterrupt:
        print("\nSaliendo...")
    except Exception as e:
        print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    main()