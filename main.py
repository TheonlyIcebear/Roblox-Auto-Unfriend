import subprocess, requests, threading, time, os
from termcolor import cprint

os.system("")

class Main:
    def __init__(self):
        self.start()

    def getXsrf(self, cookie):
        xsrfRequest = requests.post(
            "https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": cookie}
        )
        return xsrfRequest.headers["x-csrf-token"]

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def log(self, msg, msg_type=None):
        if msg_type == 'error':

            print("[", end="")
            cprint(" ERROR ", "red", end="")
            print("] ", end="")
            cprint(msg, "red")
        
        else:
            print("[", end="")
            cprint(" UNFRIENDER ", "magenta", end="")
            print("] ", end="")
            cprint(msg, "magenta")

    def check(self, cookie):
        return requests.get(
            "https://users.roblox.com/v1/users/authenticated",
            cookies={".ROBLOSECURITY": cookie},
        )

    def unfriend(self, cookie):

        self.log("Unfriending friends....")

        userid = requests.get(
            "https://users.roblox.com/v1/users/authenticated",
            cookies={".ROBLOSECURITY": cookie},
        ).json()["id"]

        friends = requests.get(
            f"https://friends.roblox.com/v1/users/{userid}/friends",
            cookies={".ROBLOSECURITY": cookie},
        ).json()["data"]

        friendIds = [friend["id"] for friend in friends]

        for friendId in friendIds:
            time.sleep(0.1)
            request = requests.post(
                f"https://friends.roblox.com/v1/users/{friendId}/unfriend",
                cookies={".ROBLOSECURITY": self.cookie},
                headers=headers,
            ).text

            if request.status_code == 200:
                self.log(f"Unfriended {friendId}")

            else:
                self.log(f"Failed to unfriend {friendId}", "error")

        self.log("Unfriended All Users!")

    def start(self):
        
        while True:
            self.log("Enter Your Cookie Below:")
            cookie = input("> ")
            check = self.check(cookie)
            if check.status_code == 200:

                self.headers = {"X-CSRF-TOKEN": self.getXsrf(cookie)}


                self.clear()
                self.unfriend(cookie)
                break

            else:
                self.log("Invalid Cookie", "error")

                time.sleep(1.4)
                self.clear()
            


if __name__ == "__main__":
    Main()
