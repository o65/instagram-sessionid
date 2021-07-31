import uuid, os, subprocess, time, calendar

clear = lambda: subprocess.call('cls||clear', shell=True)
try:
  import requests
except ImportError: 
  os.system("pip install requests")
  import requests
clear()

def login():
        username = input("[+] username: ")
        password = input("[+] password: ")
        head = {"user-agent": "Instagram 150.0.0.00.000 Android (29/10; 320dpi; 720x1491; 5912586f16aaf155/bfd0b0ddc847ea83; bfd0b0ddc8e19a25; 3a456adb43715eda; be962130f170156c; en_GB; 302733750)"}
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
