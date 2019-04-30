DEV=/dev/tty.usbserial-FA210 

web:
	python -m SimpleHTTPServer

copy:
	rshell -p ${DEV} "cp index.html /pyboard; cp app.css /pyboard; cp app.js /pyboard" 

copy-led-switcher:
	rshell -p ${DEV} "cp led-switcher.py /pyboard/main.py; cp credentials.py /pyboard"

copy-all: 
	rshell -p ${DEV} "cp index.html /pyboard; cp app.css /pyboard; cp app.js /pyboard; cp led-switcher.py /pyboard/main.py" 

rshell:
	rshell -p ${DEV}

minicom:
	minicom -s -b115200 -D ${DEV} -m -s

.PHONY: copy copy-led-switcher copy-all rshell minicom
