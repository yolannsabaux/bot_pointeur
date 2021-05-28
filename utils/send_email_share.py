import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


now = datetime.datetime.now()

def send_email(response):
    sender_email = "youradress@gmail.com" #to be changed
    receiver_email = "youradress@gmail.com" #to be changed
    password = "" #to be added

    # message to be sent
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Attendance verification {now.day}-{now.month}-{now.year} {now.hour}:{now.minute}"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = response
    text = MIMEText(text, "plain")
    message.attach(text)

    try:
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
                )
    except:
        print("Something went wrong while trying to send an email. Please contact your favorite dev.")
