# App2Date

GUI application that notifies subscribed users for any latest updates of the following technology stack:
- Python Version
- Selenium Version
- Chrome Version

Users can subscribe and recieve emails if any new updates are available, users can aslo unsubscribe to stop recieving emails



# Installation
 1. Download and install Python 3 or higher from <a href="https://www.python.org/downloads/">here</a>
 2. Clone this repo to your local machine using:
  ```bash
 git clone https://github.com/Tamer7/VersionCheck.git
 ```
 3. Navigate and open the "VersionApp" Folder in your Editor:
```bash
Folder "VersionApp"
Note: Ignore the Screenshot and Website Folder
```
 
 4. Download the required packages by typing:
 ```bash
pip install -r requirements.txt
```
 5. Download Chrome Webdriver from <a href="https://chromedriver.chromium.org/downloads">here</a>
 6. Navigate to this section of the code and replace to your Chrome Webdriver Path
``` python
self.driver = webdriver.Chrome("INSERT DRIVER PATH HERE", options=self.options)
```
 7. To recieve emails using this application, locate the "email" function, and locate the following code and change them accordinly to your sending email and password
``` python
username = Safe.username
password = Safe.password

 # CHANGE TO (Your desired sending email address, gmail preferably)
 
 username = test123@gmail.com
 password = Test12345
```

# Usage

- Type the below command to run the Application. You need to be connected to the Internet and it might take 1-5 minutes to gather the latest updates/versions from the internet so please wait patiently.
``` python
python program.py
```


- The GUI page that shows up once the application is done loading, at the left side it displays the information in rows, the green text and message's indicates that there are no new available updates, while the red text and message's indicate that there is a new available update.


![Homepage](Images/homepage.png)

- To recieve updates via email, input your email in the subscribe section and click on <b>subscribe</b> as shown and start recieving updates on email!


![](Images/emailsubscribe.png)




- To stop recieving emails, navigate to the <b>unsubscribe</b> field and input your email and click on <b>unsubscribe</b>.


![](Images/unsubscribe.png)




- You would be prompted to confirm to delete, click <b>Yes</b> to delete the email.


![](Images/popup.png)




- If you mispell your email while unsubscribing you would recieve an error as such below, just retype your email carefully and it should unsubscribe.


![](Images/unsubscribeerror.png)




# Built With

- Python - Programming Language
- Tkinter - GUI



# TODO

- Include Other Browser Support
- Optimize Code
- Resolve Bugs


# Authors

- Tamer Algarmakany (Team Leader)
- Radvan Khammud
- Ayush Arvind
- Tushar Kapoor










        

 
 
 
 
 
        
