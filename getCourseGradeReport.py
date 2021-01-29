#You must have Chocolatey installed here for this to work
##Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
#You must have Selenium Installed for this to work
##Pip command to install: pip install -U selenium

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from random import randrange
import base64
from getpass import getpass


# email = input("Enter your id:\n")
# password = getpass('Password:\n')

courseNumber = input("What is the CSC CRN of the course you are targeting?:\n")

#This is the driver for the browser of your choosing (Chrome) INSTALLING THE DRIVER IS NECESSARY TO AUTOMATE
driver = webdriver.Chrome()

#This line heads to the page you want to automate things on. Launches google chrome and heads to desired page
driver.get('https://dssapex.gsu.edu/pls/apex/f?p=114:184:::NO::P_RPT_FORMAT_184,P_LEVEL_184,P_COLG_184,P_DEPT_184,P_PREFIX_184,P_CRSNBR_184,P_TERM_184:C,%25,,,CSC,4330,202008')
sleep(3)

#Select Course Number Drop Down
driver.find_element_by_xpath('/html/body/form/div/div/div/div[5]/div/div/div[1]/div[2]/section/div[2]/div[2]/div[6]/div/div/select').click()
sleep(3)

#Select Course Number from Drop Down
select = Select(driver.find_element_by_id('P_CRSNBR_184'))
select.select_by_visible_text(courseNumber) 
sleep(3)

#Screenshot Page
driver.save_screenshot('ssn.png')
sleep(2)





