import yfinance as yf
import pandas as pd
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# ==========================
# 기본 설정
# ==========================

TICKER = "QQQ"

NAVER_EMAIL = os.environ["NAVER_EMAIL"]
NAVER_PASSWORD = os.environ["NAVER_PASSWORD"]
RECEIVE_EMAIL = os.environ["RECEIVE_EMAIL"]


# ==========================
# QQQ 데이터 가져오기
# ==========================

def get_qqq_data():

    data = yf.download(
        TICKER,
        period="3mo",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    data.columns = data.columns.get_level_values(0)

    return data


# ==========================
# 투자 신호 분석
# ==========================

def analyze():

    df = get_qqq_data()

    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA20"] = df["Close"].rolling(20).mean()
    df["VOL20"] = df["Volume"].rolling(20).mean()


    today = df.iloc[-1]
    yesterday = df.iloc[-2]


    price = float(today["Close"].iloc[0])
ma5 = float(today["MA5"].iloc[0])
ma20 = float(today["MA20"].iloc[0])

volume = float(today["Volume"].iloc[0])
avg_volume = float(today["VOL20"].iloc[0])


    message = None
    title = None


    # ==========================
    # 매수 조건
    # ==========================

    buy_signal = (
        price > ma20
        and ma5 > ma20
        and volume > avg_volume
        and price <= ma20 * 1.05
    )


    if buy_signal:

        title = "[QQQ 투자 알림] 매수 신호 발생"

        message = f"""
QQQ 매수 신호 발생

현재 가격:
${price:.2f}

5일 이동평균:
${ma5:.2f}

20일 이동평균:
${ma20:.2f}

조건:
✅ 20일선 위
✅ 5일선 > 20일선
✅ 거래량 증가
✅ 과열 구간 아님

판단:
강한 상승 추세 확인

전략:
분할 매수 검토
"""


    # ==========================
    # 매도 조건
    # ==========================

    sell_signal = (
        price < ma20
        and yesterday["Close"] < yesterday["MA20"]
        and ma5 < ma20
    )


    if sell_signal:

        title = "[QQQ 투자 알림] 매도 검토 신호"

        message = f"""
QQQ 매도 검토 신호 발생

현재 가격:
${price:.2f}

5일 이동평균:
${ma5:.2f}

20일 이동평균:
${ma20:.2f}

조건:
❌ 20일선 이탈
❌ 2일 연속 하락 추세
❌ 단기 추세 약화

판단:
상승 추세 훼손 가능성

전략:
보유 비중 축소 검토
"""


    return title, message



# ==========================
# 이메일 발송
# ==========================

def send_email(title, body):

    if body is None:
        return


    msg = MIMEMultipart()

    msg["From"] = NAVER_EMAIL
    msg["To"] = RECEIVE_EMAIL
    msg["Subject"] = title


    msg.attach(
        MIMEText(
            body,
            "plain",
            "utf-8"
        )
    )


    server = smtplib.SMTP(
        "smtp.naver.com",
        587
    )

    server.starttls()

    server.login(
        NAVER_EMAIL,
        NAVER_PASSWORD
    )


    server.send_message(msg)

    server.quit()



# ==========================
# 실행
# ==========================

if __name__ == "__main__":

    title, body = analyze()

    send_email(
        title,
        body
    )

    print("QQQ 분석 완료")
