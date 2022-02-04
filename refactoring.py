import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class Mail:
    def __init__(self, login, password):
        self.login =  login
        self.password = password
        self.headers = None

    def send_messsage(self, message, recipients, subject, adress='smtp.gmail.com'):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        identifier = smtplib.SMTP(adress, 587)
        identifier.ehlo()
        identifier.starttls()
        identifier.ehlo()
        identifier.login(self.login, self.password)
        identifier.sendmail(self.login['login'], identifier, msg.as_string())
        identifier.quit()

    def recieve_messsage(self, adress='imap.gmail.com'):
        mail = imaplib.IMAP4_SSL(adress)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.headers if self.headers else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

if __name__ == '__main__':
    letter = Mail('login@gmail.com', 'qwerty')
    letter.send_messsage('Message', ['vasya@email.com', 'petya@email.com'], 'Subject')
    letter.recieve_messsage()
