import smtplib
import ssl
import sys
from email.message import EmailMessage
from email.mime.text import MIMEText
import os
from datetime import datetime
from dotenv import load_dotenv
#import upload_report_to_cloud_storage
load_dotenv()

# Browser = sys.argv[1]
#Browser = sys.argv[1] 

email_sender = 'harunkumar411@gmail.com'
#email_password = os.getenv('GMAIL_16_DIGIT_PASSWORD')
email_password='rfhvzjplmvclldhv'
email_receiver = 'praveenkumarm214@gmail.com'


def generate_mailer_body():
    """This Method returns Email message Subject, mail Body of the mail"""
    #subject = f"Automation Status | Browser: {Browser} | {datetime.now().strftime('%d/%m/%y %I:%M %p')}"
    subject = f"Regarding Push code in GIT HUB | Browser:"
    body = f"""
    <h1>Hi  PLEASE push the updated code in Git repo so that Team can pull the code and verify thats your code is running fine .</h1>
    <p style="font-size:100px">Thanks & Regards,<br>
    Automation Team</p>
    """
    em = EmailMessage()
    html_body = MIMEText(body, 'html')
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(html_body)
    return em.as_string()


def send_mail():
    """This Method sends mail"""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, generate_mailer_body())
        print("Mail sent")
    except Exception as e:
        print(f"Exception occurred while sending mail: {e}")


send_mail()