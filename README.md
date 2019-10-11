# breakfastbot
A bot that can make you all sorts of breakfasts.


## Installation
 - Download and install [Raspbian Stretch with desktop](https://www.raspberrypi.org/downloads/raspbian/).
 - [Enable ssh on Raspbian](https://www.raspberrypi.org/documentation/remote-access/ssh/).
 - update system and reboot
```
$ sudo apt update
$ sudo apt upgrade
$ sudo reboot
```
 - Enable I2C
```
$ sudo raspi-config
$ # select "Interfacing Options" menu item
$ # select "I2C" menu item
$ sudo reboot
```
 - Connect and power on the Crickit board
 - Verify the Crickit i2c address 0x49 is found in the following commands output.
```
$ i2cdetect -y 1
```
 - install python packages
```
$ sudo apt install python3-virtualenv
$ python3 -m virtualenv -p python3 /home/pi/pyenv
$ source /home/pi/pyenv/bin/activate
$ pip install adafruit-circuitpython-crickit tornado
```


## Server
You can start either the console interface or the tornado app with the following commands.
```
$ python -m breakfastbot.console
$ python -m breakfastbot.server
```


## Video
[![demo](http://img.youtube.com/vi/gb1WkahF7os/0.jpg)](http://www.youtube.com/watch?v=gb1WkahF7os)

