import smtplib
import getpass

HOST = 'smtp-mail.outlook.com'
PORT = 587

from_email = 'muhammadsunusi909@outlook.com'
to_email = 'bsmuhammad352@gmail.com'
password = getpass.getpass('Enter your password: ')

message = f'Subject: Demo email\r\n\r\nHey, this is just a demo email\r\n'

try:
    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f'[*] Pinging the server: {status_code} {response}')

    status_code, response = smtp.starttls(context=ssl.create_default_context())
    print(f'[*] Starting tls connection: {status_code} {response}')

    status_code, response = smtp.login(from_email, password)
    print(f'[*] Loging into the server: {status_code} {response}')

    smtp.sendmail(from_email, to_email, message)
    smtp.quit()
    print('Sent')
except Exception as e:
    print(f"An error occurred: {e}")