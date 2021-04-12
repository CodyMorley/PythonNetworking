import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('mymailtest@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'codymorley'
msg['To'] = 'mailtest@mailtest.com'
msg['Subject'] = 'This is a test.'

with open ('message.txt', 'r') as mail:
    message = mail.read()

msg.attach(MIMEText(message, 'plain'))
filename = 'matrix-code.jpg'

