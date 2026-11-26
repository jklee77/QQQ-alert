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


    # 5일 전 MA20

    df["MA20_PREV"] = (
        df["MA20"]
        .shift(5)
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
# MA20 추세 판단
# =========================

def add_ma20_trend(df):


    def check_trend(row):


        if (
            pd.isna(row["MA20"])
            or
            pd.isna(row["MA20_PREV"])
        ):

            return "데이터 부족"



        if row["MA20"] > row["MA20_PREV"]:

            return "📈 상승추세"



        elif row["MA20"] < row["MA20_PREV"]:

            return "📉 하락추세"



        else:

            return "➡️ 횡보"



    df["MA20_TREND"] = (
        df.apply(
            check_trend,
            axis=1
        )
    )


    return df




# =========================
# MA20 추세 변경 감지
# =========================

def add_ma20_change(df):


    df["MA20_TREND_PREV"] = (
        df["MA20_TREND"]
        .shift(1)
    )



    def check_change(row):


        if (

            pd.isna(
                row["MA20_TREND_PREV"]
            )

            or

            row["MA20_TREND_PREV"]
            ==
            row["MA20_TREND"]

        ):

            return "변경 없음"



        return (

            row["MA20_TREND_PREV"]

            +

            " → "

            +

            row["MA20_TREND"]

        )



    df["MA20_CHANGE"] = (
        df.apply(
            check_change,
            axis=1
        )
    )


    return df




# =========================
# MA20 기울기
# =========================

def add_ma20_slope(df):


    df["MA20_SLOPE"] = (

        (

            df["MA20"]

            -

            df["MA20"].shift(5)

        )

        /

        df["MA20"].shift(5)

        *

        100

    )


    return df




# =========================
# MA20 추세 유지 일수
# =========================

def add_ma20_duration(df):


    duration = []


    count = 0


    previous = None



    for trend in df["MA20_TREND"]:


        if trend == previous:

            count += 1


        else:

            count = 1



        duration.append(
            count
        )


        previous = trend



    df["MA20_DURATION"] = duration



    return df




# =========================
# 가격 위치
# =========================

def add_price_position(df):


    def check_position(row):


        if row["Close"] > row["MA20"]:

            return "20MA 위"



        elif row["Close"] < row["MA20"]:

            return "20MA 아래"



        else:

            return "20MA 동일"



    df["PRICE_VS_MA20"] = (

        df.apply(

            check_position,

            axis=1

        )

    )


    return df




# =========================
# 거래량
# =========================

def add_volume_indicator(df):


    df["VOL20"] = (

        df["Volume"]

        .rolling(window=20)

        .mean()

    )


    return df




# =========================
# RSI
# =========================

def add_rsi(df, period=14):


    delta = df["Close"].diff()


    gain = delta.clip(
        lower=0
    )


    loss = (
        -delta.clip(
            upper=0
        )
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


    rs = (
        avg_gain /
        avg_loss
    )


    df["RSI"] = (

        100 -

        (

            100 /

            (1 + rs)

        )

    )


    return df




# =========================
# MACD
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

        ema12 -

        ema26

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
# 전체 지표 계산
# =========================

def calculate_indicators(df):


    df = add_moving_average(df)


    df = add_ma20_trend(df)


    df = add_ma20_change(df)


    df = add_ma20_slope(df)


    df = add_ma20_duration(df)


    df = add_price_position(df)


    df = add_volume_indicator(df)


    df = add_rsi(df)


    df = add_macd(df)


    return df




# =========================
# 현재 상태 요약
# =========================

def get_indicator_summary(df):


    today = df.iloc[-1]



    summary = {


        "price":

            round(

                float(today["Close"]),

                2

            ),



        "MA5":

            round(

                float(today["MA5"]),

                2

            ),



        "MA20":

            round(

                float(today["MA20"]),

                2

            ),



        "MA20_PREV":

            round(

                float(today["MA20_PREV"]),

                2

            ),



        "MA20_TREND":

            today["MA20_TREND"],



        "MA20_CHANGE":

            today["MA20_CHANGE"],



        "MA20_SLOPE":

            round(

                float(today["MA20_SLOPE"]),

                2

            ),



        "MA20_DURATION":

            int(

                today["MA20_DURATION"]

            ),



        "PRICE_VS_MA20":

            today["PRICE_VS_MA20"],



        "MA60":

            round(

                float(today["MA60"]),

                2

            ),



        "MA120":

            round(

                float(today["MA120"]),

                2

            ),



        "RSI":

            round(

                float(today["RSI"]),

                2

            ),



        "MACD":

            round(

                float(today["MACD"]),

                4

            ),



        "MACD_SIGNAL":

            round(

                float(today["MACD_SIGNAL"]),

                4

            ),



        "Volume":

            int(today["Volume"]),



        "Volume_AVG":

            int(today["VOL20"])

    }



    return summary
