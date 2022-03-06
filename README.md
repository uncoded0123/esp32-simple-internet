# esp32-simple-connect-to-internet

main.py about 5 lines of code

http1.py about 40 lines code

Connects to first wifi network if available, else it connects to second.

It's only necessary to change main.py. Insert username (aka ssid), password, and url. Returns JSON

HTTP1.py is also energy efficient. It tries to connect 300,000 times, deepsleeps 10,000 ms, retries.
