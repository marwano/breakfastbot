from adafruit_crickit import crickit
import time
from .conf import SPIN, SPOON, ROTATE_DELAY, SWING_DELAY


def rotate(direction, duration=ROTATE_DELAY):
    crickit.servo_4.angle = SPIN[direction]
    time.sleep(duration)
    crickit.servo_4.angle = SPIN['stop']


def swing(direction):
    rotate(direction, duration=SWING_DELAY)


def drop_spoon(servo_name, bottom, top):
    servo = getattr(crickit, servo_name)
    servo.angle = bottom
    time.sleep(1)
    servo.angle = top
    time.sleep(0.5)


def move(action):
    if action in ['drop_spoon_small', 'drop_spoon_big']:
        spoon = action.replace('drop_spoon_', '')
        drop_spoon(*SPOON[spoon])
    elif action in ['rotate_clockwise', 'rotate_anticlockwise']:
        direction = action.replace('rotate_', '')
        rotate(direction)
    elif action in ['swing_clockwise', 'swing_anticlockwise']:
        direction = action.replace('swing_', '')
        swing(direction)
    else:
        raise ValueError('invalid action')
