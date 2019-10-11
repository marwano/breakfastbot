import pprint
import time
import tty
import sys
import termios
from .motors import move

EXIT_KEYS = ['\x1b', '\x03']    # escape and CTRL+C
STDIN_FD = sys.stdin.fileno()
ACTIONS = {
    '1': 'rotate_clockwise',
    '3': 'rotate_anticlockwise',
    '4': 'swing_clockwise',
    '6': 'swing_anticlockwise',
    '7': 'drop_spoon_small',
    '9': 'drop_spoon_big',
}


def get_char():
    old_settings = termios.tcgetattr(STDIN_FD)
    try:
        tty.setraw(STDIN_FD)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(STDIN_FD, termios.TCSADRAIN, old_settings)


def main():
    pprint.pprint(sorted(ACTIONS.items()))
    print('Press numbers to move motors or escape/CTRL+C to exit.')
    while True:
        char = get_char()
        if char in EXIT_KEYS:
            return
        if char in ACTIONS.keys():
            move(ACTIONS[char])


if __name__ == "__main__":
    main()
