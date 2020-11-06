
import sys
import time

from djitellopy import Tello


# tello = Tello(host="192.168.0.105")
tello = Tello()
tello.connect()

ssid = sys.argv[1]
password = sys.argv[2]

tello.connect_to_wifi(ssid, password)

# tello.set_wifi_credentials("Tello_XXXX", "testing888")

time.sleep(5)
exit()
