import sqlite3


# this starts a connection and makes a file called 'email.db'
conn = sqlite3.connect("email.db")
c = conn.cursor()

# Creates a table called email
# c.execute("""CREATE TABLE email (
#       email_address text
#      )""")


conn.commit()
conn.close()
