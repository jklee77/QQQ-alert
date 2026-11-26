import os

import smtplib


from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from email.mime.image import MIMEImage




def send_email(

    html,

    chart_file=None,

    subject="📈 QQQ AI 투자 리포트"

):



    sender = os.getenv(
        "NAVER_EMAIL"
    )


    password = os.getenv(
        "NAVER_PASSWORD"
    )


    receiver = os.getenv(
        "NAVER_EMAIL"
    )



    print()

    print(
        "메일 환경 확인"
    )


    print(
        "EMAIL:",
        "***"
    )


    print(
        "PASSWORD:",
        "입력됨"
        if password
        else
        "없음"
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





    # =========================
    # 메일 생성
    # =========================


    msg = MIMEMultipart(
        "related"
    )



    msg["From"] = sender


    msg["To"] = receiver


    msg["Subject"] = subject





    # =========================
    # HTML 본문
    # =========================


    body = MIMEText(

        html,

        "html",

        "utf-8"

    )


    msg.attach(
        body
    )





    # =========================
    # 차트 이미지 첨부
    # =========================


    if chart_file:



        try:



            with open(

                chart_file,

                "rb"

            ) as f:



                img = MIMEImage(

                    f.read()

                )




            img.add_header(

                "Content-ID",

                "<qqq_chart>"

            )



            img.add_header(

                "Content-Disposition",

                "inline",

                filename="qqq_chart.png"

            )



            msg.attach(
                img
            )



            print(
                "차트 첨부 완료"
            )



        except Exception as e:



            print(

                "차트 첨부 실패:",

                e

            )






    # =========================
    # 네이버 SMTP 발송
    # =========================


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
