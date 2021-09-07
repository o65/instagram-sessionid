import uuid, os, time, calendar, random, string

try:
  import requests
except ImportError: 
  os.system("pip install requests")
  import requests

def login():
        username = input("[+] username: ")
        password = input("[+] password: ")
        head = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"}
        data = {
            "jazoest": "22452",
            "phone_id": uuid.uuid4(),
            "enc_password": f"#PWD_INSTAGRAM:0:{calendar.timegm(time.gmtime())}:{password}",
            "username": username,
            "adid": uuid.uuid4(),
            "guid": uuid.uuid4(),
            "device_id": uuid.uuid4(),
            "google_tokens": "[]",
            "login_attempt_count": "0"}
        req = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=head, data=data)
        if "logged_in_user" in req.text:
            print(f"[+] Logged In '{username}'")
            sessionid = req.cookies.get("sessionid")
            print(f"[+] sessionid: {sessionid}")
            open(f"{username}.txt","w").write(str(sessionid))
            print(f"[+] Saved in {username}.txt")
            input()
            exit()
        else:
            print(f'[-] {req.json()["message"]}')
            input()
            exit()
login()
