import smtplib
from email.mime.text import MIMEText
from time import sleep
from random import randint

login = open("login.txt", "r").read().split(',') # Other file containing login details
username = login[0]
password = login[1]

def start_server():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    return server

def send_emails(server, target):
    msg = MIMEText("Hello this is just a test message")
    msg['Subject'] = 'Hello ' + str(randint(0, 1000000)) # Adding a random number to prevent the subjects being the same
    msg['From'] = username
    msg['To'] = target
    print(msg)
    server.sendmail(username, target, msg.as_string())
    print('sended the mail')

def main(target):
    while True:
        server = start_server()
        try:
            print('Started sending emails')
            send_emails(server, target)
        except Exception as e:
            sleep(60) # To bypass gmails auto timeout system

if __name__ == "__main__":
    try:
        main('targetmail@targetprovider.de')
    except KeyboardInterrupt:
        print("Interrupted program. Exitting...")
