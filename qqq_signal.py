import yfinance as yf
import pandas as pd
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# =========================
# 환경 설정
# =========================

TICKER = "QQQ"

NAVER_EMAIL = os.environ.get("NAVER_EMAIL")
NAVER_PASSWORD = os.environ.get("NAVER_PASSWORD")
RECEIVE_EMAIL = os.environ.get("RECEIVE_EMAIL")


# =========================
# QQQ 데이터 가져오기
# =========================

def get_qqq_data():

    df = yf.download(
        TICKER,
        period="6mo",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    # yfinance 최신 버전 MultiIndex 처리
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df


# =========================
# 투자 신호 분석
# =========================

def analyze():

    df = get_qqq_data()

    if df.empty:
        return None, None


    # 이동평균 계산

    df["MA5"] = (
        df["Close"]
        .rolling(window=5)
        .mean()
    )

    df["MA20"] = (
        df["Close"]
        .rolling(window=20)
        .mean()
    )

    df["VOL20"] = (
        df["Volume"]
        .rolling(window=20)
        .mean()
    )


    today = df.iloc[-1]
    yesterday = df.iloc[-2]


    price = float(today["Close"])
    ma5 = float(today["MA5"])
    ma20 = float(today["MA20"])

    volume = float(today["Volume"])
    avg_volume = float(today["VOL20"])


    title = None
    body = None


    # =========================
    # 매수 조건
    # =========================

    buy_signal = (
        price > ma20
        and ma5 > ma20
        and volume > avg_volume
        and price <= ma20 * 1.05
    )


    if buy_signal:

        title = "[QQQ 투자 알림] 매수 신호"

        body = f"""
QQQ 매수 신호 발생

현재 가격:
${price:.2f}

5일 이동평균:
${ma5:.2f}

20일 이동평균:
${ma20:.2f}

거래량:
{volume:,.0f}

평균 거래량:
{avg_volume:,.0f}


조건:
✅ 가격이 20일선 위
✅ 5일선 > 20일선
✅ 거래량 증가
✅ 과열 구간 아님


전략:
분할 매수 검토
"""


    # =========================
    # 매도 조건
    # =========================

    sell_signal = (
        price < ma20
        and yesterday["Close"] < yesterday["MA20"]
        and ma5 < ma20
    )


    if sell_signal:

        title = "[QQQ 투자 알림] 매도 검토"

        body = f"""
QQQ 매도 검토 신호 발생

현재 가격:
${price:.2f}

5일 이동평균:
${ma5:.2f}

20일 이동평균:
${ma20:.2f}


조건:
❌ 20일 이동평균 이탈
❌ 단기 추세 약화
❌ 하락 지속 가능성


전략:
보유 비중 축소 검토
"""


    return title, body



# =========================
# 네이버 이메일 발송
# =========================

def send_email(title, body):

    if body is None:
        print("현재 투자 신호 없음")
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


    print("이메일 발송 완료")



# =========================
# 실행
# =========================

if __name__ == "__main__":

    title, body = analyze()

    send_email(
        title,
        body
    )

    print("QQQ 분석 완료")
