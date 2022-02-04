import subprocess, threading, time, os
try:
  import requests
  from termcolor import cprint
except:
  try:
    import pip
  except ImportError:
      os.system("")
      print("[", end="")
      print('\033[31m'+" ERROR ", "red", end="")
      print("] " , end="")
      print('\033[31m'+"Pip not installed. Installing now...")
      subprocess.call("curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py", shell=True)
      time.sleep(5)
      os.system("get-pip.py")
  print("[", end="")
  print('\033[31m'+" ERROR ", "red", end="")
  print("] " , end="")
  print('\033[31m'+"Packages not installed. Installing now...")
  subprocess.call("pip install termcolor", shell=True)
  subprocess.call("pip install requests", shell=True)
finally:
  import requests
  from termcolor import cprint
# Made by Ice Bear#0167
def getXsrf(cookie):
      xsrfRequest = requests.post("https://auth.roblox.com/v2/logout", cookies={
          '.ROBLOSECURITY': cookie
      })
      return xsrfRequest.headers["x-csrf-token"]
def clear():
  if os.name == 'nt':
    os.system("cls")
  else:
    os.system("clear")
class Unfriend:
  global headers
  global cookie
  def unfriend(_):
    print("[", end="")
    cprint(" UNFRIENDER ", "magenta", end="")
    print("] " , end="")
    cprint("Unfriending friends....", "magenta")
    friends = requests.get(f"https://friends.roblox.com/v1/users/{userid}/friends", cookies={'.ROBLOSECURITY': str(cookie)}).json()['data']
    friendIds = [friend['id'] for friend in friends]
    for i in friendIds:
      time.sleep(0.1)
      print(requests.post(f"https://friends.roblox.com/v1/users/{i}/unfriend",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers).text)
      print("[", end="")
      cprint(" UNFRIENDER ", "magenta", end="")
      print("] " , end="")
      cprint(f"Unfriended {i}!", "magenta")
    print("[", end="")
    cprint(" UNFRIENDER ", "magenta", end="")
    print("] " , end="")
    cprint("Unfriended All!", "magenta")
  def check(_):
    global cookie
    global message
    print("[", end="")
    cprint(" UNFRIENDER ", "magenta", end="")
    print("] " , end="")
    cprint("Enter Your Cookie Below:", 'magenta')
    cookie = input("> ")
    return requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)})
  def start(_):
    global headers
    global userid
    global goOn
    os.system("")
    check = Unfriend.check()
    if check.status_code ==200:
      headers={'X-CSRF-TOKEN': getXsrf(cookie)}
      userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
      userid = userdata['id'] #user id
      clear()
      threading.Thread(target=Unfriend.unfriend).start()
    else:
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] " , end="")
      cprint("Invalid Cookie", 'red')
      time.sleep(1.4)
      clear()
      Unfriend.check()
if __name__ == '__main__':
  Unfriend = Unfriend()
  Unfriend.start()
  # Coded by Ice Bear#0167
