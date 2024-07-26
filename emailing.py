import smtplib
import imghdr
from email.message import EmailMessage
password = "abd"
SENDER = "itqan@gmail.com"
RECEIVER = "itqan@gmail.com"
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer just showed up!"
    email_message.set_content("Hey, we just saw a new customer!")
    with open(image_path,"rb") as file:
        content = file.read()
    email_message.add_attachment(content,maintype = "image",subtype =imghdr.what(None,content))
    
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,password=password)
    gmail.sendmail(SENDER,RECEIVER,email_message.as_string())
    gmail.quit()