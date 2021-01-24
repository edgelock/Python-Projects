#You must have Chocolatey installed here for this to work
#You must have Selenium Installed for this to work
#Pip command to install: pip install -U selenium

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from random import randrange
import base64
from getpass import getpass

#Get channel name from user

email = input("Enter your email:\n")
password = getpass('Password:')
newRole = input("What would you like to name the new role?:\n")


#These line are to automate me typing in a string for a test
#Test Variables
#channelname = (randrange(100))
#channeltype = (randrange(2))

#Testing Variable for 1 or 2 selection of channel type
#channeltype = 1


#This is the driver for the browser of your choosing (Chrome) INSTALLING THE DRIVER IS NECESSARY TO AUTOMATE
driver = webdriver.Chrome()

#Create action chain object for double clicking
action = ActionChains(driver)

sleep(2)
driver.maximize_window()


#Heads over to the site you want to log into.
driver.get ('https://discord.com/channels/@me')
#Selects the field for username & password and enters strings
sleep(3)
##Add a loop to require ID/PW again if it's not correct the first time it's entered. 
driver.find_element_by_xpath ('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input').send_keys(email)
sleep(3)
driver.find_element_by_xpath ('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys(password)
sleep(3)
#Clicks the login button to enter said items
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]/div').click()
sleep(7)

#Selecting the server search field
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[1]/button').click()
sleep(2)

#Input Server name in field
driver.find_element_by_xpath ('//*[@id="app-mount"]/div[4]/div[2]/div/div/div/input').send_keys('CSC')
sleep(2)

#Click CSC General
driver.find_element_by_xpath('//*[@id="app-mount"]/div[4]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/span').click()
sleep(2)

#Right Click Series
# identifying the source element
rightClickThis = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[1]/header/h1')
# action chain object creation
action = ActionChains(driver)
# right click operation and then perform
action.context_click(rightClickThis).perform()
sleep(2)

#Select Server Settings
driver.find_element_by_xpath('/html/body/div/div[6]/div/div/div/div[7]/div[2]/div[2]/div[1]').click()
sleep(2)

#Select Roles
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/nav/div/div[3]').click()
sleep(2)

#Select Create New Role
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div/aside/div/div[1]/div/div/div[1]').click()
sleep(2)

#Select Field to type in New Role Title
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div/div/div/div[2]/div[1]/div/input').click()
sleep(2)

#Delete everything in the field 
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div/div/div/div[2]/div[1]/div/input').send_keys(Keys.CONTROL, 'a')
sleep(.5)
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div/div/div/div[2]/div[1]/div/input').send_keys(Keys.BACKSPACE)
sleep(2)

#Input New Role Title into field
driver.find_element_by_xpath ('/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div/div/div/div[2]/div[1]/div/input').send_keys(newRole)
sleep(3)

#Hit "Save Changes" after role name is entered
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/button[2]/div').click()
sleep(2)



###SECOND HALF OF THE SCRIPT
##You CTRL+/ only ONE TIME

#Find out how to run this in the same window, possibly same tab.



# #Head over to https://dyno.gg/account
# driver.get ('https://dyno.gg/account')

# #Log In Steps
# #Selects the field for username & password and enters strings
# sleep(2)
# ##Add a loop to require ID/PW again if it's not correct the first time it's entered. 
# driver.find_element_by_xpath ('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input').send_keys(email)
# sleep(3)
# driver.find_element_by_xpath ('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys(password)
# sleep(3)
# #Clicks the login button to enter said items
# driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]/div').click()
# sleep(3)

# #Select CSC General
# driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/a').click()
# sleep(3)

# #Select Modules
# driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[1]/aside/div[3]/ul/li[3]/a').click()
# sleep(3)

# #Select Autorole Settings
# driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[8]/div/a[1]').click()
# sleep(3)

# #Select Joinable Ranks
# driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/ul/li[2]/a').click()
# sleep(3)

# #Select Role Dropdown
# driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/p/span/select').click()
# sleep(3)

# #Select Role From Dropdown
# select = Select(driver.find_element_by_class_name('module-setting-dropdown'))
# select.select_by_visible_text(newRole) 
# sleep(2)

# #Click 'Add to add the role'
# driver.find_element_by_xpath('//*[@id="autoroles-settings"]/div[1]/div[1]/div/p/input').click()
# sleep(3)
