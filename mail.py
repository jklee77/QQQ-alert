import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(html):


    sender = os.environ.get(
        "NAVER_EMAIL"
    )


    password = os.environ.get(
        "NAVER_PASSWORD"
    )


    receiver = os.environ.get(
        "RECEIVE_EMAIL"
    )


    msg = MIMEMultipart(
        "alternative"
    )


    msg["Subject"] = (
        "📈 QQQ AI 투자 리포트"
    )


    msg["From"] = sender

    msg["To"] = receiver



    msg.attach(
        MIMEText(
            html,
            "html",
            "utf-8"
        )
    )


    smtp = smtplib.SMTP(
        "smtp.naver.com",
        587
    )


    smtp.starttls()


    smtp.login(
        sender,
        password
    )


    smtp.sendmail(
        sender,
        receiver,
        msg.as_string()
    )


    smtp.quit()


    print(
        "메일 발송 완료"
    )
