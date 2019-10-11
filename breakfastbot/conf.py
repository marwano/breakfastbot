from os.path import dirname
import os

PORT = 8080
APP_SETTINGS = dict(
    debug=bool(os.environ.get('APP_DEBUG')),
    template_path=(dirname(__file__) + '/templates'),
)

SPOON = dict(
    small=('servo_1', 90, 0),
    big=('servo_3', 180, 100),
)
SPIN = dict(stop=87, clockwise=80, anticlockwise=93)
ROTATE_DELAY = 0.1
SWING_DELAY = 1.4
