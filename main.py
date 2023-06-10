import urequests, http1
response = urequests.get("<website_url>")
print(response) # response.<whatever> (eg, response.text, or response.json())
response.close()
