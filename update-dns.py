import requests, sys
import random, string
import base64, datetime

# Read Config
execfile("hover.cfg")

# API Endpoint
url = "https://www.hover.com/api/login"

# Generate payload

d=str(datetime.datetime.now())
len=64
rand=""

for _ in range(len):
	rand += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)


p1 = {"timestamp":d, "key": rand}
payload_data = base64.urlsafe_b64encode(str(p1))

# sys.exit(0)
# Login
payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"+username+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+password+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

if not response.ok or "hoverauth" not in response.cookies:
	print "Login failed"
else:
	# print(response.text)
	# print(response.cookies["hoverauth"])

	# The DNS entry we want to update
	url = "https://www.hover.com/api/dns/dns16451432"
	
	payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n"+str(payload_data)+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
	headers = {
	    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
	    'Cookie': "hoverauth="+response.cookies["hoverauth"],
	    'Content-Type': "application/json",
	    'Cache-Control': "no-cache"
	    }
	
	response = requests.request("PUT", url, data=payload, headers=headers)
	
	print(response.text)
