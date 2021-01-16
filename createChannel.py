
#You must have Chocolatey installed here for this to work
#You must have Selenium Installed for this to work
#Pip command to install: pip install -U selenium

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from random import randrange
import base64

#Get server name from user
#Removing the user input part for testing purposes.
channelname = input("Enter Channel Name\n")

#These line are to automate me typing in a string for a test
#Test Variables
#channelname = (randrange(100))
#channeltype = (randrange(2))

#Testing Variable for 1 or 2 selection of channel type
#channeltype = 1


#This is the driver for the browser of your choosing (Chrome) INSTALLING THE DRIVER IS NECESSARY TO AUTOMATE
driver = webdriver.Chrome()
sleep(2)
driver.maximize_window()


#Heads over to the site you want to log into.
driver.get ('https://discord.com/channels/@me')
#Selects the field for username & password and enters strings
sleep(3)
#Need to enter your own ID/PW for server in the 2 below ".send_keys" fields.
driver.find_element_by_xpath ('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input').send_keys('')
sleep(3)
driver.find_element_by_xpath ('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys('')
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

#Click CSC General
driver.find_element_by_xpath('/html/body/div/div[6]/div/div/div/div[9]/div[1]/div').click()
sleep(2)

#  #There should be an option to select voice or text channel eventually.
# if channeltype == 1:
#     driver.find_element_by_xpath('').click()
# elif channeltype ==2:
#     driver.find_element_by_xpath('').click()

driver.find_element_by_xpath ('/html/body/div/div[4]/div[2]/div/form/div/div/div[2]/div[2]/div/input').send_keys(channelname)
sleep(3)
driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div/form/div/div/div[3]/button[1]/div').click()
sleep(4)


# #Don't even worry about this until I figure something out. 
# #Channel Creation Update
# # driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/section/div[2]/div[3]/svg/path[2]').click()
# # sleep(2)
# # driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/section/div[2]/div[3]/svg/path[2]').click()
# # sleep(2)
# # driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[4]/div/div[5]/div/div/a/div[2]').click()
# # sleep(2)
# #driver.find_element_by_xpath ('/html/body/div/div[4]/div[2]/div/form/div/div/div[2]/div[2]/div/input').send_keys( channelname + ' has been created.')
# #sleep(3)







