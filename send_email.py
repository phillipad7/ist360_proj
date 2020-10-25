import smtplib, ssl
import os
import user_list

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SENDER_HOST = 'smtp.office365.com'
SENDER_PORT = 587

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

_subject = 'Default Subject - Test Email'
_sender, _sender_pass = user_list.EMAIL_CGU, user_list.PASS_CGU
_receivers = ['catsz35@hotmail.com']
_filePath = os.path.join(__location__, 'DefaultTemplate.html')


print('__location__: {}'.format(__location__))




def _getHtml(path:str):
    # print(path)
    with open(path, 'r') as f:
        html = f.read()
    return html


def _getRcvrEmailList(receivers:list):
    return ','.join(i for i in receivers)


def _assembleHtmlEmail(subject:str, sender:str, receivers:str, filePath):
    message = MIMEMultipart()
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = _getRcvrEmailList(receivers)
    html = _getHtml(filePath)
    message.attach(MIMEText(html, _subtype='html'))

    return message
    

def sendEmail(subject=_subject, sender=_sender, sender_pass=_sender_pass, receivers=_receivers, filePath=_filePath):
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(SENDER_HOST, SENDER_PORT)
        # server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.login(sender, sender_pass)

        message = _assembleHtmlEmail(subject, sender, receivers, filePath)
        server.sendmail(sender, receivers, message.as_string())

    except Exception as e:
        print(e)
    finally:
        server.quit() 


if __name__=='__main__':
    print('-----------START--------------')

    subject = 'Test Email - Sent from Python'
    sender, sender_pass = user_list.EMAIL_CGU, user_list.PASS_CGU
    receivers = ['catsz35@hotmail.com','phil.wong@live.com']
    filePath1 = 'Template.html'



    # sendEmail(subject, sender, sender_pass, receivers, filePath1)
    sendEmail()

