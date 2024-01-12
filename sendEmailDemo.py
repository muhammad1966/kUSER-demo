import smtplib
import getpass

HOST = 'smtp.gmail.com'
PORT = 587

from_email = 'muhammadsanusi909@gmail.com'
to_email = 'bsmuhammad352@gmail.com'
password = getpass.getpass('Enter your password: ')

message = '''Subject: Demo email
Hey, this is just a demo email
'''

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print (f'[*] Echoing the server: {status_code} {response}')

status_code, response = smtp.starttls()
print (f'[*] starting tls: {status_code} {response}')

status_code, response = smtp.login(from_email, password)
print (f'[*] Loging into the server: {status_code} {response}')

smtp.sendmail(from_email, to_email, message)
smtp.quit()
