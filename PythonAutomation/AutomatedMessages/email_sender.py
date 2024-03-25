import time
import schedule
import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "slavidimitrov54@gmail.com"
    msg['from'] = user
    password = "<your password here>"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


def send_email():
    print('send email')
    email_alert("Generated email", "EVERYTHING WAS WORTH IT MY GIRL!", "damla.s.k@abv.bg")


schedule.every().day.at("23:10").do(send_email)


while True:
    schedule.run_pending()
    time.sleep(1)
