import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import platform
import time
import tkinter as tk
from tkinter import *
from database import *
import smtplib
from email.mime.text import MIMEText
from emailPass import Safe


# starts tkinter
root = Tk()
root.title("AppToDate")

# input field to get users email
user_email = Entry(root, width=25)
user_email.grid(row=3, column=0)

# input field to delete users email
email_delete = Entry(root, width=25)
email_delete.grid(row=4, column=0)


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


# this gets all emails from the database
# we will use this code and implement it into the other code once the mail functionality is ready
def emailGet():
    # Creates the connection from the database.py
    conn = sqlite3.connect("email.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM email")
    records = c.fetchall()
    print("This is all the emails in the database : " + str(records))
    global get_records
    global new_record
    get_records = ""

    for i in records:
        get_records += str(i[0] + ",")
        # print(get_records)
        new_record = get_records[:-1]
        print(new_record)

    conn.commit()
    conn.close()


# this is the email functionality to send email using smtp
def email(email, email_string):
    smtp_ssl_host = "smtp.gmail.com"
    smtp_ssl_port = 465
    username = Safe.username
    password = Safe.password
    sender = "TEAMDSQUAD"
    targets = [email]

    msg = MIMEText(email_string)
    msg["Subject"] = "Version Check Updates"
    msg["From"] = sender
    msg["To"] = ", ".join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()


def checkVersion():
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
        # calls the get email function
        emailGet()
        # this method sends email with a message
        email(str(new_record), "A new Version for Python is Available")

    if chrome_new == final_chrome:
        frame = LabelFrame(root, padx=15, pady=15)
        frame.grid(row=6, column=5)
        chromeFrame = Label(
            frame, text="You have the Latest Chrome Version : " + chrome_new
        )
        chromeFrame.grid(row=0, column=0)
    else:
        frame = LabelFrame(root, padx=15, pady=15)
        frame.grid(row=6, column=5)
        chrome_new_version = Label(
            frame,
            text="A New Chrome version : " + final_chrome + " is Available for Update",
        )
        chrome_new_version.grid(row=0, column=0)
        # calls the get email function
        emailGet()
        # this method sends email with a message
        email(str(new_record), "A new Version for Chrome is Available")

    if selenium_computer_version == final_sel:
        frame = LabelFrame(root, padx=15, pady=15)
        frame.grid(row=7, column=5)
        selFrame = Label(
            frame,
            text="You have the Latest Selenium Version : " + selenium_computer_version,
        )
        selFrame.grid(row=0, column=0)
    else:
        frame = LabelFrame(root, padx=15, pady=15)
        frame.grid(row=7, column=5)
        sel_new_Frame = Label(
            frame,
            text="A New Selenium version : " + final_sel + " is Available for Update",
        )
        sel_new_Frame.grid(row=0, column=0)
        # calls the get email function
        emailGet()
        # this method sends email with a message
        email(str(new_record), "A new Version for Selenium is Available")

    # ------------ ENDS HERE


# calling the above function to show the data on the window
checkVersion()


# refreshes for any updates
def refresh():
    checkVersion()


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


# this inserts emails into the database when the subscribe button is clicked
def submit():
    # Creates the connection from the database.py
    conn = sqlite3.connect("email.db")
    c = conn.cursor()

    # Insert into the database table
    c.execute(
        "INSERT INTO email VALUES (:email_address)", {"email_address": user_email.get()}
    )

    conn.commit()
    conn.close()

    # Clear The Text Boxes
    user_email.delete(0, END)


# this currently removes the email from the database when the unsubscribe button is clicked
# currently it removes record by id
def removeEmail():
    conn = sqlite3.connect("email.db")
    c = conn.cursor()
    if c.execute("DELETE from email WHERE oid = " + email_delete.get()):
        deleted_email = Label(
            root, text="You have been Unsubscribed from the mailing list"
        )
        deleted_email.grid(row=5, column=0)
    else:
        error_label = Label(root, text="There is no such record")
        error_label.grid(row=5, column=0)

    email_delete.delete(0, END)
    conn.commit()
    conn.close()


# button to get email

email_button = Button(root, text="Subscribe", command=submit)
email_button.grid(row=3, column=4)

# this is a test button delete later
test = Button(root, text="showemail", command=emailGet)
test.grid(row=3, column=5)
# delete later

# this is a button to refresh the window
refresh = Button(root, text="Click to Refresh", command=refresh)
refresh.grid(row=3, column=6)

# button to delete email
button_delete = Button(root, text="UnSubscribe", command=removeEmail)
button_delete.grid(row=4, column=4)

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
