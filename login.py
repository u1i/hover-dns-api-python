import requests

execfile("hover.cfg")

url = "https://www.hover.com/api/login"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"+username+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+password+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

if not response.ok or "hoverauth" not in response.cookies:
	print "Login failed"
else:
	print(response.text)
	print(response.cookies)
