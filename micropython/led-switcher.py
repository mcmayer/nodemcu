try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network
import re
from utime import sleep
import credentials

def parse_request(s):
    # a really tiny (and bad) request parser
    print(s)
    m = re.match(r'^(GET|POST) (\S+) HTTP', s.decode())
    [method, path, params] = [None, None, {}]
    if m is not None:
        try:
            method = m.group(1)
            body = m.group(2)
            spl = body.split('?')
            if len(spl) == 1:
                path = spl[0]
                params = {}
            else:
                [path, params] = spl
                params = params.split('&')
                params =  dict(map(lambda v: (v[0],v[1]), (map(lambda s: s.split('='), params)))) 
        except:
            print("Can't parse {}".format(s))
            pass
        return [method, path, params]

def do_work():
    sleep(.5) 

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(credentials.ssid, credentials.password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
for i in range(5):
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)

app_css = open("app.css", 'r').read()
app_js = open("app.js", 'r').read()
index_html = open("index.html", 'r').read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)    # all non-blocking so we can do other work
s.bind(('', 80))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
    except OSError as e:
        do_work()
        continue
    print('Connection from %s' % str(addr))
    request = None
    while request is None:
        try:
            request = conn.recv(1024)
        except OSError as e:
            do_work()
            request = None
    [method, path, params] = parse_request(request)
    print([method, path, params])
    if method == "GET" and path == "/":
        response = index_html
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
    elif method == "GET" and path == "/app.css":
        response = app_css
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/css\n')
    elif method == "GET" and path == "/app.js":
        response = app_js
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: application/javascript\n')
    elif method == "GET" and path == "/set":
        status = params.get("led")
        if status is not None:
            if status == 'on':
                led.value(0)
            elif status == 'off':        
                led.value(1)
            else:
                print("I don't understand led={}".format(status))
        response = status
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: "text/plain')
    else: 
        response = ""
        conn.send('HTTP/1.1 404 Not Found\n')
        conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    i=0
    l = len(response)
    while i<l:
        try:
            sent = conn.send(response[i:(i+256)])
        except OSError as e:
            continue
        print(sent)
        i += sent
    conn.close()
