from tkinter import font
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import platform
import time
from tkinter import *
from database import *
import smtplib
from email.mime.text import MIMEText
from emailPass import Safe
from datetime import date
import datetime
from Validator import *
from tkinter import messagebox
from PIL import ImageTk, Image
import urllib
import webbrowser


class FindVersion:
    def __init__(self, master):
        master.title("AppToDate")
        # frame = Frame(master)
        # frame.grid(row=5, column=5)

        master.geometry("1080x300")
        master.iconbitmap("logo.png")

        menu = Menu(master)
        master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Guide", command=self.redirect_doc)
        file.add_command(label="----------")
        file.add_command(label="Reset Data", command=self.reset_email_data)
        file.add_command(label="Exit", command=self.exit_application)
        menu.add_cascade(label="File", menu=file)

        # help menu in the Menu section
        help = Menu(menu)
        help.add_command(label="Feedback", command=self.feedback)
        help.add_command(label="Contact Us", command=self.contact_team)
        menu.add_cascade(label="Help", menu=help)

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
            master, text="Subscribe", command=self.subscribe, relief=RAISED
        )
        self.email_button.grid(row=3, column=2)
        self.email_button.config(height=1, width=10, background="grey")

        # button to delete email
        self.button_delete = Button(
            master, text="UnSubscribe", command=self.unsubscribe, relief=RAISED
        )
        self.button_delete.grid(row=4, column=2)
        self.button_delete.config(height=1, width=10)

        # this piece of code runs selenium without opening chrome view
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.options.add_argument("window-size=1920x1080")
        self.options.add_argument("disable-gpu")

        # REPLACE WITH YOUR WEB PATH
        # this runs google chrome webdriver, REPLACE WITH YOUR OWN WEB DRIVER PATH
        self.driver = webdriver.Chrome(
            "/Users/tamerjar/Desktop/chromedriver", options=self.options
        )
        self.driver.get("https://www.python.org/downloads/")

        time.sleep(3)

        # This  automation gets the latest version of python from the web
        self.element = self.driver.find_element(
            By.XPATH,
            '// *[ @ id = "content"] / div / section / div[1] / ol / li[1] / span[1] / a',
        )
        self.python_latest_version = self.element.text
        print("Latest Python Version: " + self.python_latest_version)

        # This  automation gets the latest version of chrome from the web
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
        """
        This functions gets the version of python, chrome and selenium
        from the users/clients device or machine.
        It throws an exception if one of the technology stacks is not
        installed on the system.

        """
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

        """
        This function compares the latest versions of (python,selenium & chrome)
        from the web against the device, and displays a message on the app if a new
        version is available or not
        NOTE:: There is an email function method included to send emails if there is
        a latest version available for an update

        """

        self.list = Listbox(master, height=1, width=60)
        self.list.grid(row=7, column=0, padx=15, pady=15)
        self.bolded = font.Font(
            weight="bold", family="Helvetica", size=14
        )  # will use the default font
        # self.list.config(font=self.bolded)

        self.lists = Listbox(master, height=1, width=60)
        self.lists.grid(row=8, column=0, padx=15, pady=15)
        self.boldeds = font.Font(
            weight="bold", family="Helvetica", size=14
        )  # will use the default font
        # self.lists.config(font=self.boldeds)

        self.list3 = Listbox(master, height=1, width=60)
        self.list3.grid(row=9, column=0, padx=15, pady=15)
        self.bolded3 = font.Font(
            weight="bold", family="Helvetica", size=14
        )  # will use the default font
        # self.list3.config(font=self.bolded3)

        # ------- THIS CODE DISPLAYS VERSION UPON RUNNING THE APP
        if self.python_latest_version == self.finalVersion:
            self.list.config(fg="green")
            self.list.insert(
                1, "You have the Latest Python Version : " + self.finalVersion
            )

        else:
            self.list.config(fg="red")
            self.list.insert(
                1,
                "PYTHON VERSION: "
                + self.python_latest_version
                + " is Available for Update",
            )

            # calls the get email function
            self.emailGet()

            # this method sends email with a message
            # checks if email exists in the database if it does it sends an email
            if self.checkMail() == True:
                self.email(
                    str(self.new_record), "A new Version for Python is Available"
                )
            else:
                print("No mail")

        if self.chrome_new == self.final_chrome:

            self.lists.config(fg="green")
            self.lists.insert(
                1, "You have the Latest Chrome Version : " + self.chrome_new
            )

        else:
            self.lists.config(fg="red")
            self.lists.insert(
                1, "CHROME VERSION: " + self.final_chrome + " is Available for Update"
            )

            # calls the get email function
            self.emailGet()
            # this method sends email with a message
            # checks if email exists in the database if it does it sends an email
            if self.checkMail() == True:
                self.email(
                    str(self.new_record), "A new Version for Chrome is Available"
                )
            else:
                print("No mail")

        if self.selenium_computer_version == self.final_sel:

            self.list3.config(fg="green")
            self.list3.insert(
                1,
                "You have the Latest Selenium Version : "
                + self.selenium_computer_version,
            )

        else:

            self.list3.config(fg="red")
            self.list3.insert(
                1, "SELENIUM VERSION: " + self.final_sel + " is Available for Update"
            )

            # calls the get email function
            self.emailGet()
            # this method sends email with a message
            # checks if email exists in the database if it does it sends an email
            if self.checkMail() == True:
                self.email(
                    str(self.new_record), "A new Version for Selenium is Available"
                )
            else:
                print("no mail")

        # ------------ ENDS HERE

    def refresh(self):
        self.displayVersions(root)

    # Inputs data from user input to database
    def subscribe(self):

        # Create an object from the Class validator to
        # check for the email validity
        self.validator = Validator(self.user_email.get())
        self.valid = self.validator.check_for_symbol()

        if (
            self.user_email.get() == ""
            or self.valid == False
            or self.check_email_exsistence() == True
        ):
            error = Label(
                root, text="Empty Field / Invalid email / Email Already Exists"
            )
            error.grid(row=1, column=1)
            error.config(fg="red")
            error.after(15000, error.destroy)
        else:
            inserted_email = Label(root, text="Email has been submitted")
            inserted_email.grid(row=1, column=1)
            inserted_email.after(7000, inserted_email.destroy)

            # Creates the connection from the database.py
            conn = sqlite3.connect("email.db")
            c = conn.cursor()
            # Insert into the database table
            c.execute(
                "INSERT INTO email VALUES (:email_address)",
                {"email_address": self.user_email.get()},
            )

            # checks for input date of emails & if greater than
            # 6 months it gets deleted
            self.date_today = date.today()
            print("Today's date : " + str(self.date_today))
            self.__delete_email_sixmonths()

            conn.commit()
            conn.close()
            self.refresh()

        # Clear The Text Boxes
        self.user_email.delete(0, END)

    # removes email when email is typed in the field of (UNSUBSCRIBE)
    def unsubscribe(self):

        self.deleteRecord = Validator(self.email_delete.get())
        self.delete = self.deleteRecord.check_for_symbol()

        if self.email_delete.get() != "":
            MsgBox = messagebox.askquestion(
                "DELETE EMAIL",
                "Are you sure you want to delete this email"
                + " "
                + str(self.email_delete.get()),
                icon="warning",
            )

            if (
                self.email_delete.get() == ""
                or self.delete == False
                or self.check_delete_existence() == False
            ):
                error_label = Label(root, text="Invalid Syntax / No record available")
                error_label.grid(row=5, column=1)
                error_label.config(fg="red")
                error_label.after(15000, error_label.destroy)

            elif MsgBox == "yes":

                conn = sqlite3.connect("email.db")
                c = conn.cursor()
                c.execute(
                    "DELETE from email WHERE email_address=?",
                    (self.email_delete.get(),),
                )
                deleted_email = Label(
                    root, text="You have been Unsubscribed from the mailing list"
                )
                deleted_email.grid(row=5, column=1)
                deleted_email.after(3000, deleted_email.destroy)
                conn.commit()
                conn.close()

        self.email_delete.delete(0, END)

    # checks for record in the db
    def checkRecordDb(self):
        conn = sqlite3.connect("email.db")
        c = conn.cursor()
        c.execute("SELECT * FROM email")
        self.rows = c.fetchall()
        self.email_check = ""

        for self.row in self.rows:
            self.email_check += str(self.row[0] + ",")
            print(self.email_check)

        conn.commit()
        conn.close()

    def emailGet(self):
        # Creates the connection from the database.py
        conn = sqlite3.connect("email.db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM email")
        self.records = c.fetchall()
        print("This is all the emails in the database : " + str(self.records))
        self.get_records = ""

        for self.i in self.records:
            self.get_records += str(self.i[0] + ",")
            # print(get_records)
            self.new_record = self.get_records[:-1]
            print(self.new_record)

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

    def check_email_exsistence(self):
        """
        This function ensures that no duplicate data/email is stored in the database
        It gets the input and checks if it exists in the database, if True meaning it already exist
        else if false meaning it doesnt exist
        """

        self.email_exists = False
        conn = sqlite3.connect("email.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM email WHERE email_address = :email_address",
            {"email_address": self.user_email.get()},
        )

        # Previous line selects a row of your database only if the column that contains
        # the email adress in said row has the same address as the one from the entry

        if (
            c.fetchone()
        ):  # which is the same as saying "if c.fetchone retrieved something in it"
            self.email_exists = True

        else:
            self.email_exists = False

        conn.commit()
        conn.close()

        return self.email_exists

    def check_delete_existence(self):

        """
        This function checks if the input from the unsubscribe matches the data in the database
        If it does, it return a false and the data can be deleted
        """

        self.delete_exist = False

        conn = sqlite3.connect("email.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM email WHERE email_address = :email_address",
            {"email_address": self.email_delete.get()},
        )

        if c.fetchone():
            self.delete_exist = True
        else:
            self.delete_exist = False

        conn.commit()
        conn.close()

        return self.delete_exist

    def feedback(self):
        # replace with feeback link
        webbrowser.open("https://google.com")

    def reset_email_data(self):

        """
        Displays a message box upon running of this function,
        if the user clicks yes all the data in the database
        would get deleted

        """

        MsgBox = messagebox.askquestion(
            "DELETE RECORDS",
            "Are you sure you want to delete all email data",
            icon="warning",
        )

        if MsgBox == "yes":
            conn = sqlite3.connect("email.db")
            c = conn.cursor()

            c.execute("DELETE FROM email")
            conn.commit()
            conn.close()

        else:
            print("do nothing")

    def checkMail(self):
        """
        This function returns True if email exists int the database and False if it doesnt,
        It is used to validate before sending an email to the user
        """
        self.mail_exists = False
        conn = sqlite3.connect("email.db")
        c = conn.cursor()
        c.execute("SELECT * FROM email")

        if c.fetchone():
            self.mail_exists = True
        else:
            self.mail_exists = False

        return self.mail_exists

    def exit_application(self):
        exit()

    def redirect_doc(self):
        # link to readme page on github
        webbrowser.open("https://github.com/Tamer7/VersionCheck/blob/master/README.md")

    def contact_team(self):
        # link to page for contacting team
        pass


root = Tk()
app = FindVersion(root)
app.versionSystem()
app.displayVersions(root)
app.checkRecordDb()


root.mainloop()
