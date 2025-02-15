import imaplib

email = "prashanthps7013@gmail.com"
password = "ENTER GMAIL APP PASSWORD"
print("Check emails")
M = imaplib.IMAP4_SSL('imap.gmail.com')
print(M.login(email, password))
print(M.list())
print(M.select('inbox'))

