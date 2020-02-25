import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import platform
import time
import tkinter
from tkinter import *

# starts tkinter
root = Tk()
root.title("AppToDate")

# input field to get users email
user_email = Entry(root, width = 25)
user_email.pack()

# this runs google chrome webdriver, REPLACE WITH YOUR OWN WEB DRIVER PATH
driver = webdriver.Chrome("/Users/tamerjar/Desktop/chromedriver")
driver.get("https://www.python.org/downloads/")

time.sleep(3)

# This selenium automation gets the latest version of python from the web
element = driver.find_element(By.XPATH, '// *[ @ id = "content"] / div / section / div[1] / ol / li[1] / span[1] / a')
chrome_latest_version = element.text
print("Latest Python Version: " + chrome_latest_version)

# This selenium automation gets the latest version of chrome from the web
driver.get("https://chromedriver.chromium.org/downloads")
time.sleep(3)
chrome = driver.find_element(By.XPATH, '//*[@id="sites-canvas-main-content"]/table/tbody/tr/td/div/div[4]/h2/span/a')
final_chrome = chrome.text
print("Latest Chrome Version: " + final_chrome)


# This Automation gets latest version of selenium from the web
driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
sel = driver.find_element(By.XPATH, '/html/body/div[3]/table/tbody/tr[3]/td[2]')
final_sel = sel.text
print("Latest Selenium Version: " + final_sel)

# finds pythons version on system on system
try:
    pythonVersion = platform.python_version()
    finalVersion = "Python " + pythonVersion
    # Python Version on your system
    print("Your Version: " + finalVersion)
except:
    print("Python is not installed on your system")

# code for getting chrome current version on system
try:
    chrome_version = driver.capabilities['browserVersion']
    chrome_new = "ChromeDriver " + chrome_version
    # Chrome Version on your system
    print("Your Chrome Version: " + chrome_new)
except:
    print("Chrome is not installed on your system")

# code for getting selenium current version on system
try:
    selenium_computer_version = selenium.__version__
    # Selenium Version on your system
    print("Your Selenium Version " + selenium_computer_version)
except:
    print("Selenium is not installed on your system")


# ------- THIS CODE DISPLAYS VERSION UPON RUNNING THE APP
if (chrome_latest_version == finalVersion):
    frame = LabelFrame(root, padx=25, pady=25)
    frame.pack()
    pythonFrame = Label(frame, text= "No Version for python is Available")
    pythonFrame.grid(row=0, column=0)
else:
    frame = LabelFrame(root, padx=25, pady=25)
    frame.pack()
    python_new_version = Label(frame, text = "A New Version for python is Available")
    python_new_version.grid(row=0, column=0)



if (chrome_new == final_chrome):
    frame = LabelFrame(root, padx=25, pady=25)
    frame.pack()
    chromeFrame = Label(frame, text= "No Version for Chrome is Available")
    chromeFrame.grid(row=0, column=0)
else:
    frame = LabelFrame(root, padx=25, pady=25)
    frame.pack()
    chrome_new_version = Label(frame, text = "A New Version for Chrome is Available")
    chrome_new_version.grid(row=0, column=0)


if (selenium_computer_version == final_sel):
    frame = LabelFrame(root, padx=25, pady=25)
    frame.pack()
    selFrame = Label(frame, text= "No Version for Selenium is Available")
    selFrame.grid(row=0, column=0)
else:
    frame = LabelFrame(root, padx=25, pady=25)
    frame.pack()
    sel_new_Frame = Label(frame, text= "No Version for Selenium is Available")
    sel_new_Frame.grid(row=0, column=0)

#------------ ENDS HERE




# function to check if new version is available fro python when the button is clicked
def getPython():
    # checks if new version is available for python
    if (chrome_latest_version == finalVersion):
        my_label = Label(root, text = "No Version for python is Available")
        my_label.pack()
    else:
        my_other = Label(root, text = "A New Version for python is Available")
        my_other.pack()


# function to check if new version is available fro chrome when the button is clicked
def getChrome():
    # checks if new version is available for Chrome
    if (chrome_new == final_chrome):
        my_chrome = Label(root, text = "No New Chrome Version Available")
        my_chrome.pack()
    else:
        new_chrome = Label(root, text = "A new Chrome Version is Available")
        new_chrome.pack()


# function to check if new version is available fro selenium when the button is clicked
def getSelenium():

    if (selenium_computer_version == final_sel):
        my_label_selenium = Label(root, text= "No New Selenium Version is Available")
        my_label_selenium.pack()
    else:
        new_selenium = Label(root, text = "A new Selenium Version is Available")
        new_selenium.pack()


# gets email and stores it in variable email
def getEmail():
    email = user_email.get()
    if user_email != "":
        show_message = Label(root, text = "Email Submitted")
        show_message.pack()
    else:
        print("Empty text field")
    print(email)



#button to get email

email_button = Button(root, text = "Submit Email", command = getEmail)
email_button.pack()

#button for python
my_label_python = Button(root, text = "Check Version For Python", command = getPython)
my_label_python.pack()

#button for chrome
my_label_chrome = Button(root, text = "Check Version for Chrome", command = getChrome)
my_label_chrome.pack()

#button for seleniun

my_selenium_button = Button(root, text = "Check Version for Selenium", command = getSelenium)
my_selenium_button.pack()




root.mainloop()




