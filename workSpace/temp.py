import dht
import machine
from time import sleep

d = dht.DHT22(machine.Pin(18))

while True:
  m = d.measure()
  t = d.temperature()
  h = d.humidity()

  
  print("Temperatura: ", t)
  print("Humidade: ", h)
  

  sleep(1.0)

