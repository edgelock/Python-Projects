import pyautogui

#Sets the password (or answer) to the gui prompt
secret = "turtle"
#Leaves the password field empty
password = ""

#While the password the user enters does not equal the previously set secret the user will be prompted for a password
while password != secret:
    password = pyautogui.password('Enter password (text will be hidden)')

#Once a password that is entered matches the secret, the while loop will break and the password will be shown
print("Cracked, password is " + secret)
