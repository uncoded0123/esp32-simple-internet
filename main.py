import urequests, connect

def send(x):
    response = urequests.get("url/" + str(x))
    response.close()

def recieve():
    response = urequests.get('url')
    return response.text # or response.json(), etc.)
