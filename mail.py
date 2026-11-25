import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(html):


    print()

    print("메일 환경 확인")


    sender = os.getenv(
        "NAVER_EMAIL"
    )


    password = os.getenv(
        "NAVER_PASSWORD"
    )


    receiver = os.getenv(
        "NAVER_EMAIL"
    )


    print(
        "EMAIL:",
        "***"
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
            "수신 이메일 없음"
        )



    msg = MIMEMultipart()


    msg["From"] = sender

    msg["To"] = receiver

    msg["Subject"] = "QQQ AI 투자 리포트"



    msg.attach(
        MIMEText(
            html,
            "html",
            "utf-8"
        )
    )



    try:


        server = smtplib.SMTP_SSL(

            "smtp.naver.com",

            465

        )


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



        print()

        print(
            "메일 발송 성공"
        )



    except Exception as e:


        print()

        print(
            "메일 발송 실패:",
            e
        )


        raise
