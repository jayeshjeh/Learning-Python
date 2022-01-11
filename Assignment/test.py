import requests
resp = requests.get("http://olympus.realpython.org")
html = resp.text
print(html[86:132])
