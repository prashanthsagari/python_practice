import smtplib
import getpass


smtp_object = smtplib.SMTP('smtp.gmail.com', 587)  # Correct usage

print('*********************')
print(smtp_object.ehlo())
print(smtp_object.starttls()) # Upgrade to TLS

# email = getpass.getpass('Email:')
# password = getpass.getpass('Password please:')

email = "prashanthps7013@gmail.com"
password = "ENTER GMAIL APP PASSWORD"
print(smtp_object.login(email, password))

msg = "Subject: Title" +  "\n" +  "Hello Prashanth"
smtp_object.sendmail(email, email, msg)
print("Email Sent")


