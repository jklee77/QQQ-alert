import pandas as pd


# =========================
# 이동평균 계산
# =========================

def add_moving_average(df):

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

    df["MA60"] = (
        df["Close"]
        .rolling(window=60)
        .mean()
    )

    df["MA120"] = (
        df["Close"]
        .rolling(window=120)
        .mean()
    )

    return df



# =========================
# 거래량 분석
# =========================

def add_volume_indicator(df):

    df["VOL20"] = (
        df["Volume"]
        .rolling(window=20)
        .mean()
    )

    return df



# =========================
# RSI 계산
# =========================

def add_rsi(df, period=14):

    delta = df["Close"].diff()

    gain = delta.clip(lower=0)

    loss = (
        -delta.clip(upper=0)
    )


    avg_gain = (
        gain
        .rolling(period)
        .mean()
    )

    avg_loss = (
        loss
        .rolling(period)
        .mean()
    )


    rs = avg_gain / avg_loss


    df["RSI"] = (
        100 -
        (100 / (1 + rs))
    )


    return df



# =========================
# MACD 계산
# =========================

def add_macd(df):

    ema12 = (
        df["Close"]
        .ewm(
            span=12,
            adjust=False
        )
        .mean()
    )


    ema26 = (
        df["Close"]
        .ewm(
            span=26,
            adjust=False
        )
        .mean()
    )


    df["MACD"] = (
        ema12 - ema26
    )


    df["MACD_SIGNAL"] = (
        df["MACD"]
        .ewm(
            span=9,
            adjust=False
        )
        .mean()
    )


    return df



# =========================
# 전체 지표 적용
# =========================

def calculate_indicators(df):

    df = add_moving_average(df)

    df = add_volume_indicator(df)

    df = add_rsi(df)

    df = add_macd(df)

    return df



# =========================
# 현재 상태 분석
# =========================

def get_indicator_summary(df):

    today = df.iloc[-1]


    summary = {

        "price":
            round(float(today["Close"]),2),

        "MA5":
            round(float(today["MA5"]),2),

        "MA20":
            round(float(today["MA20"]),2),

        "MA60":
            round(float(today["MA60"]),2),

        "MA120":
            round(float(today["MA120"]),2),

        "RSI":
            round(float(today["RSI"]),2),

        "MACD":
            round(float(today["MACD"]),4),

        "MACD_SIGNAL":
            round(float(today["MACD_SIGNAL"]),4),

        "Volume":
            int(today["Volume"]),

        "Volume_AVG":
            int(today["VOL20"])
    }


    return summary
