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
from datetime import date
import datetime


class FindVersion:
    def __init__(self, master):
        master.title("AppToDate")
        frame = Frame(master)
        frame.grid(row=5, column=5)

        label_text = Label(master, text="Enter your email here : ")
        label_text.grid(row=1, column=0)

        # label unsubscribe from the email list
        label_text_uns = Label(master, text="Unsubscribe by typing in your email : ")
        label_text_uns.grid(row=2, column=0)

        self.user_email = Entry(root, width=25)
        self.user_email.grid(row=1, column=1)

        # input field to delete users email
        self.email_delete = Entry(root, width=25)
        self.email_delete.grid(row=2, column=1)

        # button to get email

        email_button = Button(root, text="Subscribe", command=self.submit)
        email_button.grid(row=1, column=2)

        # button to delete email
        button_delete = Button(root, text="UnSubscribe", command=self.removeEmail)
        button_delete.grid(row=2, column=2)

        # this piece of code runs selenium without opening chrome view
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.options.add_argument("window-size=1920x1080")
        self.options.add_argument("disable-gpu")

        # this runs google chrome webdriver, REPLACE WITH YOUR OWN WEB DRIVER PATH
        self.driver = webdriver.Chrome(
            "/Users/tamerjar/Desktop/chromedriver", options=self.options
        )
        self.driver.get("https://www.python.org/downloads/")

        time.sleep(3)

        # This selenium automation gets the latest version of python from the web
        self.element = self.driver.find_element(
            By.XPATH,
            '// *[ @ id = "content"] / div / section / div[1] / ol / li[1] / span[1] / a',
        )
        self.python_latest_version = self.element.text
        print("Latest Python Version: " + self.python_latest_version)

        # This selenium automation gets the latest version of chrome from the web
        self.driver.get("https://chromedriver.chromium.org/downloads")
        time.sleep(3)
        self.chrome = self.driver.find_element(
            By.XPATH,
            '//*[@id="sites-canvas-main-content"]/table/tbody/tr/td/div/div[4]/h2/span/a',
        )
        self.final_chrome = self.chrome.text
        print("Latest Chrome Version: " + self.final_chrome)

        # This Automation gets latest version of selenium from the web
        self.driver.get("https://www.selenium.dev/downloads/")
        time.sleep(3)
        self.sel = self.driver.find_element(
            By.XPATH, "/html/body/div[3]/table/tbody/tr[3]/td[2]"
        )
        self.final_sel = self.sel.text
        print("Latest Selenium Version: " + self.final_sel)

    def versionSystem(self):
        # finds pythons version on system on system
        try:
            self.pythonVersion = platform.python_version()
            self.finalVersion = "Python " + self.pythonVersion
            # Python Version on your system
            print("Your Version: " + self.finalVersion)
        except:
            print("Python is not installed on your system")

        # code for getting chrome current version on system
        try:
            self.chrome_version = self.driver.capabilities["browserVersion"]
            self.chrome_new = "ChromeDriver " + self.chrome_version
            # Chrome Version on your system
            print("Your Chrome Version: " + self.chrome_new)
        except:
            print("Chrome is not installed on your system")

        # code for getting selenium current version on system
        try:
            self.selenium_computer_version = selenium.__version__
            # Selenium Version on your system
            print("Your Selenium Version " + self.selenium_computer_version)
        except:
            print("Selenium is not installed on your system")

    def displayVersions(self, master):

        # ------- THIS CODE DISPLAYS VERSION UPON RUNNING THE APP
        if self.python_latest_version == self.finalVersion:
            pythonFrame = Label(
                master, text="You have the Latest Python Version : " + self.finalVersion
            )
            pythonFrame.grid(row=0, column=0)
        else:
            frame = LabelFrame(root, padx=15, pady=15)
            frame.grid(row=5, column=2)
            self.python_new_version = Label(
                frame,
                text="A New Python version : "
                + self.python_latest_version
                + " is Available for Update",
            )
            self.python_new_version.grid(row=0, column=0)
            # calls the get email function
            self.emailGet()
            # this method sends email with a message
            self.email(str(new_record), "A new Version for Python is Available")

        if self.chrome_new == self.final_chrome:
            frame = LabelFrame(master, padx=15, pady=15)
            frame.grid(row=6, column=2)
            self.chromeFrame = Label(
                frame, text="You have the Latest Chrome Version : " + self.chrome_new
            )
            self.chromeFrame.grid(row=0, column=0)
        else:
            frame = LabelFrame(master, padx=15, pady=15)
            frame.grid(row=6, column=2)
            self.chrome_new_version = Label(
                frame,
                text="A New Chrome version : "
                + self.final_chrome
                + " is Available for Update",
            )
            self.chrome_new_version.grid(row=0, column=0)
            # calls the get email function
            self.emailGet()
            # this method sends email with a message
            self.email(str(new_record), "A new Version for Chrome is Available")

        if self.selenium_computer_version == self.final_sel:
            frame = LabelFrame(master, padx=15, pady=15)
            frame.grid(row=7, column=2)
            self.selFrame = Label(
                frame,
                text="You have the Latest Selenium Version : "
                + self.selenium_computer_version,
            )
            self.selFrame.grid(row=0, column=0)
        else:
            frame = LabelFrame(master, padx=15, pady=15)
            frame.grid(row=7, column=2)
            self.sel_new_Frame = Label(
                frame,
                text="A New Selenium version : "
                + self.final_sel
                + " is Available for Update",
            )
            self.sel_new_Frame.grid(row=0, column=0)
            # calls the get email function
            self.emailGet()
            # this method sends email with a message
            self.email(str(new_record), "A new Version for Selenium is Available")

        # ------------ ENDS HERE

    def refresh(self):
        self.displayVersions(root)

    # Inputs data from user input to database
    def submit(self):
        # Creates the connection from the database.py
        conn = sqlite3.connect("email.db")
        c = conn.cursor()

        # Insert into the database table
        if c.execute(
            "INSERT INTO email VALUES (:email_address)",
            {"email_address": self.user_email.get()},
        ):
            # deletes email if longer than 6 months
            # self.delete_email_sixmonths()
            # global input_date
            # input_date = date.today()
            inserted_email = Label(root, text="Email has been submitted")
            inserted_email.grid(row=2, column=1)

        else:
            error = Label(root, text="Error entering email")
            error.grid(row=2, column=1)

        conn.commit()
        conn.close()
        self.refresh()

        # Clear The Text Boxes
        self.user_email.delete(0, END)

    # removes email when email is typed in the field of (UNSUBSCRIBE)
    def removeEmail(self):
        conn = sqlite3.connect("email.db")
        c = conn.cursor()
        if c.execute(
            "DELETE from email WHERE email_address=?", (self.email_delete.get(),)
        ):
            deleted_email = Label(
                root, text="You have been Unsubscribed from the mailing list"
            )
            deleted_email.grid(row=5, column=0)
        else:
            error_label = Label(root, text="There is no such record")
            error_label.grid(row=5, column=0)

        self.email_delete.delete(0, END)
        conn.commit()
        conn.close()

    # checks for record in the db
    def checkRecordDb(self):
        global email_check
        conn = sqlite3.connect("email.db")
        c = conn.cursor()
        c.execute("SELECT * FROM email")
        rows = c.fetchall()
        email_check = ""

        for row in rows:
            email_check += str(row[0] + ",")
            print(email_check)

        conn.commit()
        conn.close()

    # (for testing purposes only)
    def emailGet(self):
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
    def email(self, email, email_string):
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

    # funtion to delete email after 6 months
    def delete_email_sixmonths(self):
        date_exceed = input_date + datetime.timedelta(6 * 365 / 12)
        print(date_exceed)

        if date.today() >= date_exceed:
            c.execute("DELETE * from email")
        else:
            print("Email still Valid")

        conn.commit()
        conn.close()


root = Tk()
app = FindVersion(root)
app.versionSystem()
app.displayVersions(root)
app.checkRecordDb()


root.mainloop()
