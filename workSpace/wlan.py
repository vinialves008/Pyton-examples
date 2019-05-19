import urequests
import network
import ujson
from time import sleep

# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('Iot Smart House', 'IotSmartHousei8#!')


print("ok")

name = "Vinicius Alves"
temp = 0.00
humid = 70

data = {"nome": name, "temp": temp, "humid": humid}
json = ujson.dumps(data)

headers = {'Content-Type': 'application/json'}
print(json)

while True:
  response = urequests.post("http://192.168.101.69:8080/temphumid/send", data=json, headers=headers)
  print("send")
  print(response.text)
  sleep(2.0)
# now use sockets as usual





