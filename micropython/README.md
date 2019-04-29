#NodeMCU

## Prerequisites

```bash
pip3 install esptool rshell
```

## Flash micropython firmware

Download firmware from [micropython.org](http://micropython.org/download#esp8266).

[https://nodemcu.readthedocs.io/en/master/flash/](https://nodemcu.readthedocs.io/en/master/flash/)

```bash
esptool.py --port /dev/tty.usbserial-FA210 write_flash -fm qio 0x00000 esp8266-20190125-v1.10.bin
```

## Run REPL

```bash
minicom -s -b115200 -D/dev/tty.usbserial-FA210
```

