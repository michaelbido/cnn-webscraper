import selenium, datetime
from selenium import webdriver
# selenium package is used to automate web browser interaction from Python.
# webdriver helps controlling and nagivate throught the browser
# datetime is to get the current date and time, as shown below
print("Time of web request")
print(datetime.datetime.now())
# create instance of browser, request cnn
browser = webdriver.Chrome()
browser.get("http://www.cnn.com")
# select all div's under the div with zn__container class
containers = browser.find_elements_by_xpath('//div[@class="zn__containers"]/div')
# for each div under the container div
for categories in containers:
    # get text under nested div
    category = categories.text.encode('ascii', 'ignore').splitlines()
    # if the text is not empty
    if (len(category) != 0):
        #check if the category matches what we are lookin for, then print if so
        if (category[0] == "Tech") or (category[0] == "Entertainment") or (category[0] == "Travel"):
           print("---------------------------------------")            
           print(categories.text.encode('ascii', 'ignore'))
# -----------------------------
# Michael Bido-Chavez (euid: mb0501)
# CSCE 4444  - Fall 2017
# Homework 1 - Program
# Due Nov 4 by Midnight
# - - - - - - - - - - - - - - -
# # Description
#     This program creates an instance of Chrome to
#     to load the dynamic elements of CNN's webpage.
#     Then, using selenium's webdriver, finds instances of 
#     divs of class zn_containers. Then, for each of the 
#     divs inside them, select the text nested inside that falls
#     under the category of Tech, Entertainment or Travel.
#     From the script that runs this, the data is fowarded 
#     into an ouput file.
# -----------------------------


