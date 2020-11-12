import smtplib, ssl
import os
import threading
import time
import schedule

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup

import user_list
import detection_db as db


SENDER_HOST = 'smtp.office365.com'
SENDER_PORT = 587

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

_subject = 'Default Subject - Test Email'
_sender, _sender_pass = user_list.EMAIL_CGU, user_list.PASS_CGU
_receivers = ['catsz35@hotmail.com']
_inFilePath = os.path.join(__location__, 'DefaultTemplate.html')
_outFilePath = os.path.join(__location__, 'output.html')

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
    

def sendEmail(subject=_subject, sender=_sender, sender_pass=_sender_pass, receivers=_receivers, filePath=_outFilePath):
    context = ssl.create_default_context()

    try:
        # threading.Timer(30, sendEmail).start()

        server = smtplib.SMTP(SENDER_HOST, SENDER_PORT)
        # server.ehlo() # Can be omitted
        server.starttls(context=context)
        server.login(sender, sender_pass)

        message = _assembleHtmlEmail(subject, sender, receivers, filePath)
        server.sendmail(sender, receivers, message.as_string())

        print('Email Sent')

    except Exception as e:
        print(e)
    finally:
        server.quit() 


def updateHTML():
    detect=['human','cat','err']
    dt = db.fetch()


    with open(_inFilePath,'r') as fh:        
        html = open(_inFilePath).read()
        soup = BeautifulSoup(html, 'lxml')
        sqlResult = soup.find(id='sqlResult')
        sqlResult.string=''
        # print(sqlResult)

        for id, tp, date in dt:
            child = soup.new_tag('p', class_="child")
            child.string = '{:<5} {:<9} {}'.format(id,detect[tp],date)
            sqlResult.append(child)

        # print(soup.prettify())

    html = soup.prettify("utf-8")
    with open("output.html", "wb") as file:
        file.write(html)

    return True

if __name__=='__main__':
    print('\n-----------START--------------\n')

    subject = 'Test Email - Sent from Python'
    sender, sender_pass = user_list.EMAIL_CGU, user_list.PASS_CGU
    receivers = ['catsz35@hotmail.com','phil.wong@live.com']
    filePath1 = 'Template.html'

    # sendEmail(subject, sender, sender_pass, receivers, filePath1)
    sendEmail()

    # updateHTML()

#----------------------------------------------------------------------------------

    def job():
        print('Im... It is {}'.format(datetime.now()))
        return

    # schedule.every(1).minutes.at(":19").do(job)
    # schedule.every(1).minutes.at(":30").do(sendEmail)
    schedule.every().day.at("17:00").do(sendEmail)

    while True:
        schedule.run_pending()
        # time.sleep(1)
        time.sleep(3600)

    