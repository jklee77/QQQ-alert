import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(html):


    sender = os.getenv(
        "NAVER_EMAIL"
    )

    password = os.getenv(
        "NAVER_PASSWORD"
    )

    receiver = os.getenv(
        "RECEIVE_EMAIL"
    )


    print("메일 환경 확인")

    print(
        "EMAIL:",
        sender
    )

    print(
        "PASSWORD:",
        "입력됨" if password else "없음"
    )

    print(
        "RECEIVER:",
        receiver
    )



    if not sender:

        raise Exception(
            "NAVER_EMAIL 없음"
        )


    if not password:

        raise Exception(
            "NAVER_PASSWORD 없음"
        )


    if not receiver:

        raise Exception(
            "RECEIVE_EMAIL 없음"
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



    server = smtplib.SMTP(
        "smtp.naver.com",
        587
    )


    server.starttls()



    server.login(
        sender,
        password
    )



    server.sendmail(
        sender,
        receiver,
        msg.as_string()
    )



    server.quit()



    print(
        "메일 발송 완료"
    )
