import pandas as pd 
import smtplib

e = pd.read_excel("email.xlsx")
email = e['email'].values

print(email)

server = smtplib.SMTP ("smtp.gmail.com",587)
server.starttls()
server.login("xxxx@gmail.com", "xxxx")
msg ="HAI"


subject ="Hello"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in email:
    server.sendmail("xxxxxgmail.com", email, body)
server.quit()

# https://www.youtube.com/watch?v=qHyE4YAFIv0
