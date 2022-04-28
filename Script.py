import pyautogui
import time


def wait():
    time.sleep(5)
    

def moveAround():
    for key in "dadawsdadaawsdaddad":
        press(key)


def press(key):
    pyautogui.keyDown(key)
    time.sleep(2)
    pyautogui.keyUp(key)
    time.sleep(0.3)


print("Valorant Farmer by CipherKill but remade by Martisic.\n")
print("[!] Make sure you are in Fullscreen-Windowed in 1920x1080 and in the menu.")
print("[+] It's recommended to put the max fps of the game at 15FPS")
print("[!] Assurez vous d'être en Plein écran fenêtre et en 1920x1080 et dans le menu.")
print("[+] Il est recommendé de limiter les IPS/FPS du jeu à 15IPS/FPS.")
print("-"*20)
input("\nPress Enter to start program... - Appuyer sur Entrer pour commencer..\n")
print("After 5 seconds the script will start GO IN VALORANT!")
print("Après 5 secondes le script va se lancer, ALLER DANS VALORANT!")


time.sleep(5)
i=int(0)
while(True):
    i=i+1
    pyautogui.moveTo(1000, -500)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1000, 100)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1000, 1000)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1200, 500)
    pyautogui.click()
    print("[Moving]")
    moveAround()
