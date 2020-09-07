from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

# SMTP_SERVER = 'smtp.gmail.com'
# SMTP_PORT = 465
# SMTP_USER = 'dlxoghkqwer@gmail.com'
# # 실제 비밀번호를 입력해야 합니다.
# SMTP_PASSWORD = ''

SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 465
SMTP_USER = 'jlee4@naver.com'
# 실제 비밀번호를 입력해야 합니다.
SMTP_PASSWORD = input('Enter your ' + SMTP_SERVER.split('.')[1] + " password : ")

def send_mail(rcv_name, rcv_addr, contents, attachment=False):
    msg = MIMEMultipart('alternative')

    if attachment:
        msg = MIMEMultipart('mixed')

    msg['From'] = 'lthlovelee <%s>'%SMTP_USER
    msg['To'] = rcv_addr
    msg['Subject'] = rcv_name + '님, 메일이 도착했습니다.'

    text = MIMEText(contents)
    msg.attach(text)

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application', 'octet-stream')
        f = open(attachment, 'rb')
        file_contents = f.read()
        file_data.set_payload(file_contents)
        encoders.encode_base64(file_data)

        from os.path import basercv_name
        filercv_name = basercv_name(attachment)
        file_data.add_header('Content-Disposition',
                'attachment', filercv_name=filercv_name)
        msg.attach(file_data)

    smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, rcv_addr, msg.as_string())
    smtp.close()
