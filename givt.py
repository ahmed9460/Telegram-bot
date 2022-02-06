import requests
import random
littale = "qwertyuiopasdfghjklzxcvbnm"

user = input("[?] Username :")


email = "".join(random.choice(littale) for _ in range(6)) + "@gmail.com"
url = "https://core.poprey.com/api/create_test_order_v2.php"
headers = {
    "Host": "core.poprey.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-AUTH-TOKEN": "null",
    "X-TARGET-LANG": "en",
    "X-IDENTITY-TOKEN": "k4QllXMjn6Cprlq6T6kvQxTKLQ9Co84W",
    "Content-Length": "105",
    "Origin": "https://poprey.com",
    "Connection": "keep-alive",
    "Referer": "https://poprey.com/instagram_followers"
}
data = {
    "service": "Followers",
    "email": email,
    "username": user,
    "system": "Instagram",
    "count": '10',
    "type": "t1",
    "csrf":""
}

r = requests.post(url,headers=headers,data=data)
if '{"result":"Ok",' in r.text:
    print("[+] Done")
else:
    print(r.text)


