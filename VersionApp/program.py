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
        # frame = Frame(master)
        # frame.grid(row=5, column=5)

        self.credentials = Label(
            master, text="CREDENTIAL SECTION", font="Helvetica 22 bold"
        )
        self.credentials.grid(row=1, column=0)

        self.label_text = Label(
            master, text="Enter your email here:", font="Helvetica 18"
        )
        self.label_text.grid(row=3, column=0)

        # label unsubscribe from the email list
        self.label_text_uns = Label(
            master, text="Unsubscribe by typing in your email:", font="Helvetica 18"
        )
        self.label_text_uns.grid(row=4, column=0)

        # input field to insert email
        self.user_email = Entry(master, width=30)
        self.user_email.grid(row=3, column=1)

        # input field to delete users email
        self.email_delete = Entry(master, width=30)
        self.email_delete.grid(row=4, column=1)

        # button to get email

        self.email_button = Button(
            master, text="Subscribe", command=self.submit, relief=RAISED
        )
        self.email_button.grid(row=3, column=2)

        # button to delete email
        self.button_delete = Button(
            master, text="UnSubscribe", command=self.removeEmail, relief=RAISED
        )
        self.button_delete.grid(row=4, column=2)

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
            pythonFrame.grid(row=6, column=0)
        else:
            frame = LabelFrame(root, padx=25, pady=25, width=25, relief="solid")
            frame.grid(row=6, column=0)
            self.python_new_version = Label(
                frame,
                text="PYTHON VERSION: "
                + self.python_latest_version
                + " is Available for Update",
            )
            self.python_new_version.grid(row=0, column=0)
            # calls the get email function
            self.emailGet()
            # this method sends email with a message
            self.email(str(new_record), "A new Version for Python is Available")

        if self.chrome_new == self.final_chrome:
            frame = LabelFrame(master, padx=15, pady=15, width=25, relief="solid")
            frame.grid(row=7, column=0)
            self.chromeFrame = Label(
                frame, text="You have the Latest Chrome Version : " + self.chrome_new
            )
            self.chromeFrame.grid(row=0, column=0)
        else:
            frame = LabelFrame(master, padx=15, pady=15, width=25, relief="solid")
            frame.grid(row=7, column=0)
            self.chrome_new_version = Label(
                frame,
                text="CHROME VERSION: "
                + self.final_chrome
                + " is Available for Update",
            )
            self.chrome_new_version.grid(row=0, column=0)
            # calls the get email function
            self.emailGet()
            # this method sends email with a message
            self.email(str(new_record), "A new Version for Chrome is Available")

        if self.selenium_computer_version == self.final_sel:
            frame = LabelFrame(master, padx=15, pady=15, width=25, relief="solid")
            frame.grid(row=8, column=0)
            self.selFrame = Label(
                frame,
                text="You have the Latest Selenium Version : "
                + self.selenium_computer_version,
            )
            self.selFrame.grid(row=0, column=0)
        else:
            frame = LabelFrame(master, padx=15, pady=15, width=25, relief="solid")
            frame.grid(row=8, column=0)
            self.sel_new_Frame = Label(
                frame,
                text="SELENIUM VERSION: " + self.final_sel + " is Available for Update",
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

        if self.user_email.get() == "":
            error = Label(root, text="Empty Field / Invalid email")
            error.grid(row=1, column=1)
        else:
            # Creates the connection from the database.py
            conn = sqlite3.connect("email.db")
            c = conn.cursor()
            # Insert into the database table
            c.execute(
                "INSERT INTO email VALUES (:email_address)",
                {"email_address": self.user_email.get()},
            )
            # deletes email if longer than 6 months

            inserted_email = Label(root, text="Email has been submitted")
            inserted_email.grid(row=1, column=1)

            self.date_today = date.today()
            print("Today's date : " + str(self.date_today))
            self.__delete_email_sixmonths()

            self.refresh()
            conn.commit()
            conn.close()

        # Clear The Text Boxes
        self.user_email.delete(0, END)

    # removes email when email is typed in the field of (UNSUBSCRIBE)
    def removeEmail(self):
        if self.email_delete.get() == "":
            error_label = Label(root, text="Invalid Syntax / No record available")
            error_label.grid(row=5, column=1)

        else:
            conn = sqlite3.connect("email.db")
            c = conn.cursor()
            c.execute(
                "DELETE from email WHERE email_address=?", (self.email_delete.get(),)
            )
            deleted_email = Label(
                root, text="You have been Unsubscribed from the mailing list"
            )
            deleted_email.grid(row=5, column=1)
            conn.commit()
            conn.close()

        self.email_delete.delete(0, END)

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
    def __delete_email_sixmonths(self):
        date_exceed = self.date_today + datetime.timedelta(6 * 365 / 12)
        print(date_exceed)

        if date.today() >= date_exceed:
            conn = sqlite3.connect("email.db")
            c = conn.cursor()

            c.execute("DELETE * from email")
            conn.commit()
            conn.close()
        else:
            print("Email still Valid")


root = Tk()
app = FindVersion(root)
app.versionSystem()
app.displayVersions(root)
app.checkRecordDb()


root.mainloop()
