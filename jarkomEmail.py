import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "me_@gmail.com"
receive_email = "you_@gmail.com"
password = 'my_passEmail'
message = MIMEMultipart("alternative")
message["Subject"] = "Latihan Email"
message["From"] = sender_email
message["To"] = receive_email
text = """\
    text here
    """
part1 = MIMEText(text, "html")
message.attach(part1)
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receive_email, message.as_string())
        print('sending is successful..')
except:
        print('sending is failed..')
