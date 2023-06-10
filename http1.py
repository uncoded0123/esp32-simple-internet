import time, network
station = network.WLAN(network.STA_IF)
station.active(True)
while station.isconnected() == False:
    station.connect("<SSID", "Password")
    time.sleep(1)
print("Connected!")
