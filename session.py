import uuid, os, subprocess

clear = lambda: subprocess.call('cls||clear', shell=True)
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

clear()


red,white,cyan=fg("red"),fg("white"),fg("cyan")

def login():
    username = input("</> username: ")
    password = input("</> password: ")
    head = {
        "User-Agent": f'Instagram 130.0.0.00.000 (iPhone12,12; iPhone OS 12; en_US; en) AppleWebKit/600',
        "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'uuid': uuid.uuid4(),
        'password': password,
        'username': username,
        'device_id': uuid.uuid4(),
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }
    req = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=head, data=data)
    if "logged_in_user" in req.text:
        print(f'{cyan}</> logged in "{username}"')
        print(f'\n{req.cookies.get("sessionid")}')
        open(f"{username}.txt","w").write(str(req.cookies.get("sessionid")))
    elif "Incorrect Username" in req.text:
        print(f"{red}<!> The username you entered doesn't belong to an account. Please check your username and try again.")
        input()
        exit()
    elif 'Incorrect password' in req.text:
        print(f"{red}<!> Sorry, your password was incorrect. Please double-check your password.")
        input()
        exit()
    elif 'checkpoint_challenge_required' in req.text:
        print(f"{red}<!> checkpoint_required")
        input()
        exit()
    else:
        print(f'{red}<!> {req.text}')
        input()
        exit()

login()
