import pyautogui
import time

def record():
    return pyautogui.position()

def wait():
    time.sleep(5)
    
def press(key):
    pyautogui.keyDown(key)
    time.sleep(2)
    pyautogui.keyUp(key)
    time.sleep(0.3)
    
def moveAround():
    for key in "dadawsdadaawsdaddad":
        press(key)

print("*"*20)
print("Valorant Farmer by CipherKill remade by Martisic")
print("*"*20)
print("[!] It's recommended to prevent the bot not clicking")
print("[!] Click on the top Play Button and go back")
print("[!] Click on the Deathmatch button and go back")
print("[!] Click on the start button and stop matchmaking instantly")
print("[!] Click on the Invite Friends button and go back")
print("[!] If it's not working restart your game")

print("\n\n[!] Make sure you are in FullScreen-Windowed")
print("-"*20)
input("\nPress Enter to start program...\n")
input("Tell where the location of 'Play' button on the top")
topplay=record()
input("Tell where the location of 'Deathmatch' button ")
deathbutton=record()
input("Tell where the location of 'Start' button")
playAgain=record()
input("Tell where the location of 'Friends Invite' button ")
menuami=record()
print("\nPress CTRL-C to stop. \n")
time.sleep(1)
print("Farming in progress... ")
time.sleep(0.5)
print("[!]Shift to VALORANT now! You have 7 seconds to go on Valorant. ")
print("\nUSE CTRL+C OR CTRL+Z TO STOP PROGRAM\n")

time.sleep(7)
print("Enjoy :)")
i=int(0)
while(True):
    i=i+1
    print("[Starting]:",i)
    pyautogui.click(topplay)
    print("[Clicked Play]")
    time.sleep(1)
    print("[Clicked Deathmatch]")
    pyautogui.click(deathbutton)
    time.sleep(1)
    pyautogui.click(playAgain)
    print("[Clicked Launch]")
    time.sleep(1)
    print("[Clicked Friends]")
    pyautogui.click(menuami)
    time.sleep(1)

    print("[Moving]")
    moveAround()
    
