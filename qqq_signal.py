import yfinance as yf
import pandas as pd
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


TICKER = "QQQ"

NAVER_EMAIL = os.environ["NAVER_EMAIL"]
NAVER_PASSWORD = os.environ["NAVER_PASSWORD"]
RECEIVE_EMAIL = os.environ["RECEIVE_EMAIL"]



# ==========================
# 데이터 가져오기
# ==========================

def get_data():

    df = yf.download(
        TICKER,
        period="6mo",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    df.columns = df.columns.get_level_values(0)

    return df



# ==========================
# RSI 계산
# ==========================

def calculate_rsi(series, period=14):

    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi



# ==========================
# 분석
# ==========================

def analyze():

    df = get_data()


    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA20"] = df["Close"].rolling(20).mean()

    df["VOL20"] = (
        df["Volume"]
        .rolling(20)
        .mean()
    )


    df["RSI"] = calculate_rsi(
        df["Close"]
    )


    # 볼린저밴드

    df["STD20"] = (
        df["Close"]
        .rolling(20)
        .std()
    )

    df["BB_UPPER"] = (
        df["MA20"]
        +
        df["STD20"] * 2
    )


    today = df.iloc[-1]


    price = float(today["Close"])
    ma5 = float(today["MA5"])
    ma20 = float(today["MA20"])

    volume = float(today["Volume"])
    avg_volume = float(today["VOL20"])

    rsi = float(today["RSI"])

    upper = float(today["BB_UPPER"])



    score = 0

    report = []


    # 추세 점수

    if price > ma20:
        score += 1
        report.append("✅ 현재가 20일선 위")

    else:
        report.append("❌ 현재가 20일선 아래")



    if ma5 > ma20:
        score += 1
        report.append("✅ 단기 상승 추세")

    else:
        score -= 1
        report.append("❌ 단기 약세")



    if ma20 > float(df["MA20"].iloc[-5]):
        score += 1
        report.append("✅ 20일선 상승")



    # RSI 점수

    if 50 <= rsi < 70:

        score += 2
        report.append(
            f"✅ RSI 정상 상승 ({rsi:.1f})"
        )

    elif rsi >= 70:

        report.append(
            f"⚠ RSI 과열 ({rsi:.1f})"
        )

    else:

        score -= 1
        report.append(
            f"❌ RSI 약세 ({rsi:.1f})"
        )



    # 거래량

    if volume > avg_volume:

        score += 1
        report.append(
            "✅ 거래량 증가"
        )



    # 볼린저 위험

    if price < upper:

        score += 1
        report.append(
            "✅ 과열 구간 아님"
        )

    else:

        report.append(
            "⚠ 볼린저 상단 돌파"
        )



    if score >= 6:

        status = "🟢 강한 매수 후보"

    elif score >=4:

        status = "🟡 관심 구간"

    elif score <= -2:

        status = "🔴 위험 구간"

    else:

        status = "⚪ 관망"



    title = (
        f"[QQQ 투자 분석] {status}"
    )


    message = f"""
QQQ 투자 분석 리포트


현재 가격:
${price:.2f}


투자 점수:
{score} / 7


판단:
{status}


분석 내용:
"""

    for r in report:
        message += "\n" + r


    message += """

전략:
점수 기반 분할 대응


※ 본 알림은 투자 참고용입니다.
"""


    return title, message




# ==========================
# 이메일 발송
# ==========================

def send_email(title, body):


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

    print("QQQ 점수 분석 완료")
