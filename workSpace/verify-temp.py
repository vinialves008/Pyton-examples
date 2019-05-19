import dht
import machine
from time import sleep



led = machine.Pin(2, Pin.OUT)

d = dht.DHT22(machine.Pin(18))

while True:
  m = d.measure()
  t = d.temperature()
  h = d.humidity()

  
  
  print("Temperatura: ", t)
  print("Humidade: ", h)
  
  if (t >= 26):
    print("Cuidado temperatura em: ", t)
    led.value(1)
  else:
    print("Temperatura normal.")
    led.value(0)
  sleep(1.0)

