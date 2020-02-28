import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import platform
import time
from tkinter import *


# starts tkinter
root = Tk()
root.title("AppToDate")

# input field to get users email
user_email = Entry(root, width=25)
user_email.grid(row=3, column=0)


# this piece of code runs selenium without opening chrome view
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")


# this runs google chrome webdriver, REPLACE WITH YOUR OWN WEB DRIVER PATH
driver = webdriver.Chrome("/Users/tamerjar/Desktop/chromedriver", options=options)
driver.get("https://www.python.org/downloads/")

time.sleep(3)

# This selenium automation gets the latest version of python from the web
element = driver.find_element(
    By.XPATH,
    '// *[ @ id = "content"] / div / section / div[1] / ol / li[1] / span[1] / a',
)
python_latest_version = element.text
print("Latest Python Version: " + python_latest_version)

# This selenium automation gets the latest version of chrome from the web
driver.get("https://chromedriver.chromium.org/downloads")
time.sleep(3)
chrome = driver.find_element(
    By.XPATH,
    '//*[@id="sites-canvas-main-content"]/table/tbody/tr/td/div/div[4]/h2/span/a',
)
final_chrome = chrome.text
print("Latest Chrome Version: " + final_chrome)


# This Automation gets latest version of selenium from the web
driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
sel = driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[3]/td[2]")
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
    chrome_version = driver.capabilities["browserVersion"]
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
if python_latest_version == finalVersion:
    frame = LabelFrame(root, padx=15, pady=15)
    frame.grid(row=5, column=5)
    pythonFrame = Label(
        frame, text="You have the Latest Python Version : " + finalVersion
    )
    pythonFrame.grid(row=0, column=0)
else:
    frame = LabelFrame(root, padx=15, pady=15)
    frame.grid(row=5, column=5)
    python_new_version = Label(
        frame,
        text="A New Python version : "
        + python_latest_version
        + " is Available for Update",
    )
    python_new_version.grid(row=0, column=0)


if chrome_new == final_chrome:
    frame = LabelFrame(root, padx=15, pady=15)
    frame.grid(row=5, column=6)
    chromeFrame = Label(
        frame, text="You have the Latest Chrome Version : " + chrome_new
    )
    chromeFrame.grid(row=0, column=0)
else:
    frame = LabelFrame(root, padx=15, pady=15)
    frame.grid(row=5, column=6)
    chrome_new_version = Label(
        frame,
        text="A New Chrome version : " + final_chrome + " is Available for Update",
    )
    chrome_new_version.grid(row=0, column=0)


if selenium_computer_version == final_sel:
    frame = LabelFrame(root, padx=15, pady=15)
    frame.grid(row=5, column=7)
    selFrame = Label(
        frame,
        text="You have the Latest Selenium Version : " + selenium_computer_version,
    )
    selFrame.grid(row=0, column=0)
else:
    frame = LabelFrame(root, padx=15, pady=15)
    frame.grid(row=6, column=7)
    sel_new_Frame = Label(
        frame, text="A New Selenium version : " + final_sel + " is Available for Update"
    )
    sel_new_Frame.grid(row=0, column=0)

# ------------ ENDS HERE


# function to check if new version is available fro python when the button is clicked
def getPython():
    # checks if new version is available for python
    if python_latest_version == finalVersion:
        my_label = Label(root, text="No Version for python is Available")
        my_label.grid(row=8, column=0)
    else:
        my_other = Label(root, text="A New Version for python is Available")
        my_other.grid(row=8, column=0)


# function to check if new version is available fro chrome when the button is clicked
def getChrome():
    # checks if new version is available for Chrome
    if chrome_new == final_chrome:
        my_chrome = Label(root, text="No New Chrome Version Available")
        my_chrome.grid(row=10, column=0)
    else:
        new_chrome = Label(root, text="A new Chrome Version is Available")
        new_chrome.grid(row=10, column=0)


# function to check if new version is available fro selenium when the button is clicked
def getSelenium():

    if selenium_computer_version == final_sel:
        my_label_selenium = Label(root, text="No New Selenium Version is Available")
        my_label_selenium.grid(row=12, column=0)
    else:
        new_selenium = Label(root, text="A new Selenium Version is Available")
        new_selenium.grid(row=12, column=0)


# gets email and stores it in variable email
def getEmail():
    email = user_email.get()
    if user_email != "":
        show_message = Label(root, text="Email Submitted")
        show_message.grid(row=3, column=5)
    else:
        print("Empty text field")
    print(email)


# button to get email

email_button = Button(root, text="Submit Email", command=getEmail)
email_button.grid(row=3, column=4)

# button for python
my_label_python = Button(root, text="Check Version For Python", command=getPython)
my_label_python.grid(row=7, column=0)

# button for chrome
my_label_chrome = Button(root, text="Check Version for Chrome", command=getChrome)
my_label_chrome.grid(row=9, column=0)

# button for seleniun

my_selenium_button = Button(
    root, text="Check Version for Selenium", command=getSelenium
)
my_selenium_button.grid(row=11, column=0)


root.mainloop()
