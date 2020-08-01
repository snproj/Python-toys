import requests
import time

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#getMe = requests.get("https://api.telegram.org/bot{}/getMe".format(token)).json()
#print(getMe)
#print(getMe["ok"])


getUpdates = requests.get("https://api.telegram.org/bot{}/getUpdates".format(token)).json()
print(getUpdates)
latest_id = getUpdates["result"][-1]["update_id"]
print("STARTING ID: " + "{}".format(latest_id))
targetID = getUpdates["result"][-1]["message"]["chat"]["id"]
print("TARGET ID: " + "{}".format(targetID))

class Howitzer:
    def __init__(self):
        self.legs = "CLOSED"
        self.barrel = "UNSWUNG"
        self.wheels_horizontal = "IN LINE"
        self.wheels_vertical = "DOWN"
        self.embedded = "NOT EMBEDDED"
        self.firing_platform = "UP"
    def sitrep(self):
        report = """
        SITREP
        _______________
        LEGS: {}
        BARREL: {}
        WHEELS: {} AND {}
        {}
        FIRING PLATFORM: {}""".format(self.legs, self.barrel, self.wheels_horizontal, self.wheels_vertical, self.embedded, self.firing_platform)
        print_text(report)
    def swing_barrel(self):
        if self.barrel == "SWUNG":
            print_text("Barrel has already been swung!")
        else:
            self.barrel = "SWUNG"
            print_text("Barrel has been swung.")
    def unswing_barrel(self):
        if self.legs == "CLOSED":
            if self.barrel == "UNSWUNG":
                print_text("Barrel has not yet been swung!")
            else:
                self.barrel = "UNSWUNG"
                print_text("Barrel has been swung back for towing.")
        else:
            print_text("You need to close the legs first!")
    def open_legs(self):
        if self.barrel == "SWUNG":
            if self.wheels_vertical == "DOWN":
                if self.wheels_horizontal == "LEFT":
                    if self.legs == "OPEN":
                        print_text("Legs already open.")
                    else:
                        self.legs = "OPEN"
                        print_text("Legs have been opened.")
                else:
                    print_text("You need to wheels-left first!")
            else:
                print_text("You need to wheels-down first!")
        else:
            print_text("You need to swing the barrel first!")
    def close_legs(self):
        # does not need a check for swung?
        if self.barrel == "SWUNG":
            if self.wheels_vertical == "DOWN":
                if self.wheels_horizontal == "LEFT":
                    if self.legs == "CLOSED":
                        print_text("Legs already closed.")
                    else:
                        self.legs = "CLOSED"
                        print_text("Legs have been closed.")
                else:
                    print_text("You need to wheels-left first!")
            else:
                print_text("You need to wheels-down first!")
        else:
            "ERROR: How has the barrel not yet been swung?"
    def wheels_left(self):
        if self.wheels_vertical == "DOWN":
            if self.wheels_horizontal != "LEFT":
                if self.wheels_horizontal == "RIGHT":
                    self.wheels_horizontal = "IN LINE"
                    print_text("Wheels in line.")
                elif self.wheels_horizontal == "IN LINE":
                    self.wheels_horizontal = "LEFT"
                    print_text("Wheels left.")
            else:
                print_text("Wheels already left!")
        else:
            print_text("You need to wheels-down first!")
    def wheels_right(self):
        if self.wheels_vertical == "DOWN":
            if self.wheels_horizontal != "RIGHT":
                if self.wheels_horizontal == "LEFT":
                    self.wheels_horizontal = "IN LINE"
                    print_text("Wheels in line.")
                elif self.wheels_horizontal == "IN LINE":
                    self.wheels_horizontal = "RIGHT"
                    print_text("Wheels right.")
            else:
                print_text("Wheels already right!")
        else:
            print_text("You need to wheels-down first!")
    def wheels_in_line(self):
        if self.wheels_vertical == "DOWN":
            if self.wheels_horizontal != "IN LINE":
                self.wheels_horizontal = "IN LINE"
                print_text("Wheels in line.")
            else:
                print_text("Wheels already in line!")
        else:
            print_text("You need to wheels-down first!")
    def wheels_up(self):
        if self.wheels_horizontal == "IN LINE":
            if self.wheels_vertical != "UP":
                self.wheels_vertical = "UP"
                print_text("Wheels up.")
            else:
                print_text("Wheels are already up!")
        else:
            print_text("You need the wheels to be in line first!")
    def wheels_down(self):
        # does not need a check for wheels-in-line?
        if self.firing_platform == "UP":
            if self.wheels_vertical != "DOWN":
                self.wheels_vertical = "DOWN"
                print_text("Wheels down.")
                if self.embedded == "EMBEDDED":
                    self.embedded = "NOT EMBEDDED"
                    print_text("Howitzer is no longer embedded.")
            else:
                print_text("Wheels are already down!")
        else:
            print_text("You need to raise the firing platform first!")
    def embed(self):
        if self.wheels_vertical == "UP" and self.barrel == "SWUNG" and self.legs == "OPEN":
            if self.embedded != "EMBEDDED":
                self.embedded = "EMBEDDED"
                print_text("Howitzer embedded.")
            else:
                print_text("Already embedded!")
        else:
            print_text("You cannot embed the gun yet!")
    def firing_platform_down(self):
        if self.wheels_vertical == "UP" and self.barrel == "SWUNG" and self.legs == "OPEN" and self.embedded:
            if self.firing_platform != "DOWN":
                self.firing_platform = "DOWN"
                print_text("Firing platform down.")
            else:
                print_text("Firing platform is already down!")
        else:
            print_text("You cannot lower the firing platform yet!")
    def firing_platform_up(self):
        if self.firing_platform != "UP":
            self.firing_platform = "UP"
            print_text("Firing platform up.")
        else:
            print_text("Firing platform is already up!")
    def report_gun_ready(self):
        if self.firing_platform == "DOWN":
            print_text("Ready to fire!")
        else:
            print_text("Not yet ready to fire!")
    def action_front(self):
        self.legs = "OPEN"
        self.barrel = "SWUNG"
        self.wheels_horizontal = "IN LINE"
        self.wheels_vertical = "UP"
        self.embedded = "EMBEDDED"
        self.firing_platform = "DOWN"
        print_text("Gun action-fronted.")
    def cease_fire(self):
        self.legs = "CLOSED"
        self.barrel = "UNSWUNG"
        self.wheels_horizontal = "IN LINE"
        self.wheels_vertical = "DOWN"
        self.embedded = "NOT EMBEDDED"
        self.firing_platform = "UP"
        print_text("Gun cease-fired.")

howitzer = Howitzer()

def print_text(message):
    sendMessage = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token, targetID, message))

while True:
    getUpdates = requests.get("https://api.telegram.org/bot{}/getUpdates".format(token)).json()
    if getUpdates["result"][-1]["update_id"] != latest_id:
        getUpdates = requests.get("https://api.telegram.org/bot{}/getUpdates?offset={}".format(token, latest_id+1)).json()
        received_msg = getUpdates["result"][0]["message"]["text"]
        latest_id = getUpdates["result"][-1]["update_id"]
        print("MESSAGE RECEIVED: " + received_msg)
        if received_msg == "/swingbarrel":
            howitzer.swing_barrel()
        elif received_msg == "/unswingbarrel":
            howitzer.unswing_barrel()
        elif received_msg == "/openlegs":
            howitzer.open_legs()
        elif received_msg == "/closelegs":
            howitzer.close_legs()
        elif received_msg == "/wheelsleft":
            howitzer.wheels_left()
        elif received_msg == "/wheelsright":
            howitzer.wheels_right()
        elif received_msg == "/wheelsinline":
            howitzer.wheels_in_line()
        elif received_msg == "/embed":
            howitzer.embed()
        elif received_msg == "/wheelsup":
            howitzer.wheels_up()
        elif received_msg == "/wheelsdown":
            howitzer.wheels_down()
        elif received_msg == "/firingplatformup":
            howitzer.firing_platform_up()
        elif received_msg == "/firingplatformdown":
            howitzer.firing_platform_down()
        elif received_msg == "/reportgunready":
            howitzer.report_gun_ready()
        elif received_msg == "/sitrep":
            howitzer.sitrep()
        elif received_msg == "/actionfront":
            howitzer.action_front()
        elif received_msg == "/ceasefire":
            howitzer.cease_fire()
        elif received_msg == "/help":
            help_msg = """
            COMMANDS:
            _______________
            /swingbarrel
            /unswingbarrel
            /openlegs
            /closelegs
            /wheelsleft
            /wheelsright
            /wheelsinline
            /wheelsup
            /wheelsdown
            /embed
            /firingplatformup
            /firingplatformdown
            /reportgunready
            /actionfront
            /ceasefire
            /sitrep"""
            print_text(help_msg)
        else:
            print_text("ERROR: COMMAND NOT RECOGNIZED.")


    time.sleep(1)


#getUpdates2 = requests.get("https://api.telegram.org/bot{}/getUpdates?offset={}".format(token, starting_id+1)).json()
#print(getUpdates2)
#targetID = getUpdates["result"][0]["message"]["chat"]["id"]

#sendMessage = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=hello".format(token, targetID))
#print(sendMessage.json())