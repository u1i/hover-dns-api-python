import requests, sys
import random, string
import base64, datetime

def sj_do():
    username=""
    password=""

    sj = [ "Don't trust the atoms - they make up everything", "It's hard to explain puns to kleptomaniacs because they always take things literally.", "Nostalgia ain't what it used to be.", "Is there another word for 'pseudonym'?", "I used to think the brain was the most important organ. Then I thought, look what's telling me that.", "A magician was walking down the street and turned into a grocery store.", "A blind man walks into a bar. And a table. And a chair.", "What's the best part about living in Switzerland? Not sure, but the flag is a big plus.", "Two fish are in a tank. One turns to the other and asks 'How do you drive this thing?'", "Pampered cows produce spoiled milk.", "Learn sign language, it's very handy.", "I started a band called 999 Megabytes - we haven't gotten a gig yet.", "What is the difference between ignorance and apathy? I don't know, and I don't care.", "Dwarfs and midgets have very little in common.", "How do you make Holy water? Boil the hell out of it.", "I wondered why the frisbee was getting bigger, and then it hit me.", "At first I didn't know how to fasten the seatbelt. Then it clicked.", "I totally understand how batteries feel because I'm rarely ever included in things either.", "I invented a new word: Plagiarism" ]

    joke = sj[random.randint(0,len(sj))]

    dstr=str(datetime.datetime.now()) + " UTC"

    p1 = {"timestamp":dstr, "joke": joke}

    payload_data = base64.urlsafe_b64encode(str(p1))

    # API Endpoint
    url = "https://www.hover.com/api/login"

	# Login
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"+username+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+password+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW", 'Cache-Control': "no-cache"}
    response = requests.request("POST", url, data=payload, headers=headers)

    if not response.ok or "hoverauth" not in response.cookies:
        return "Hover Login failed"
    else:
        # The DNS entry we want to update
        url = "https://www.hover.com/api/dns/dns16458511"
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n"+str(payload_data)+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW", 'Cookie': "hoverauth="+response.cookies["hoverauth"], 'Content-Type': "application/json", 'Cache-Control': "no-cache"}
        response = requests.request("PUT", url, data=payload, headers=headers)

        return str(joke)
