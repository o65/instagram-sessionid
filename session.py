import uuid, os
try:
  import requests
except ImportError: 
  os.system("pip install requests")
  import requests
try: 
  from colored import fg
except ImportError:
  os.system("pip install colored")
  from colored import fg
def e():
  input()
  exit(0)
red,white,cyan=fg("red"),fg("white"),fg("cyan")
def login():
    global steps
    username=input(f"</> username: ")
    password=input("</> password: ")
    login_url = 'https://i.instagram.com/api/v1/accounts/login/'
    head = {
        'User-Agent': 'Instagram 135.0.0.34.124 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        'uuid': uuid.uuid4(),
        'password': password,
        'username': username,
        'device_id': uuid.uuid4(),
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'}
    req = requests.post(login_url, headers=head, data=data)
    if "logged_in_user" in req.text:
        print(f"{cyan}<!> logged in @{username}")
        sessionid = req.cookies.get("sessionid")
        print(f"\n{white}{sessionid}")
        open(f"{username}.txt","w").write(str(sessionid))
    elif "Incorrect Username" in req.text:
        print(f"{red}<!> The username you entered doesn't belong to an account. Please check your username and try again.")
        e()
    elif 'Incorrect password' in req.text:
        print(f"{red}<!> Sorry, your password was incorrect. Please double-check your password.")
        e()
    elif 'checkpoint_challenge_required' in req.text:
        print(f"{red}<!> checkpoint_challenge_required")
        e()
    else:
        print(f"{red}<!> {req.text}")
        e()
login()
      
