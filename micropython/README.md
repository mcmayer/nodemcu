# MicroPython on NodeMCU

## Prerequisites

```bash
pip3 install esptool rshell
```

## Flash micropython firmware

As described in the [NodeMCU docs](https://nodemcu.readthedocs.io/en/master/flash) download firmware from [micropython.org](http://micropython.org/download#esp8266) and flash it with the `esptool`:

```bash
esptool.py --port /dev/tty.usbserial-FA210 write_flash -fm qio 0x00000 esp8266-20190125-v1.10.bin
```

## Run REPL

```bash
minicom -s -b115200 -D/dev/tty.usbserial-FA210
```

## MQTT

[MQTT & MicroPython](https://www.hackster.io/bucknalla/mqtt-micropython-044e77)

```bash
https://raw.githubusercontent.com/pycom/pycom-libraries/master/examples/mqtt/mqtt.py
```

Then in rshell `cp mqtt.py /pyboard/`. (Start rshell like so: `rshell -p /dev/tty.usbserial-FA210`.)

## Go back to Arduino

Erase the flash and all will be good for using the Arduino IDE:

```bash
esptool.py --port /dev/tty.usbserial-FA210 erase_flash
```

## LED Switcher App

The following files constitute the LED Switcher App:

- `index.html`: Web page with one radio button
- `app.css`: CSS for the web page, mostly for styling the radio button.
- `app.js`: A [vuejs](https://vuejs.org/) app that controls the radio button.
- `credentials.py`: User-created file that contains WIFI ssid and password
- `led-switcher.py`: This will be `main.py` on the NodeMCU.

Create a file `credentials.py` with this content:

```python
ssid = 'your-ssid-here'
password = 'your-password-here'
```

It will be read by `led-switcher.py`.

Copy everything over using `rshell`:

```bash
make copy-all
```

Press the reset button once to activate the new code.

When WIFI registration is complete the LED blinks a few times.