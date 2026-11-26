def calculate_final_score(

    indicator,

    macro_score,

    fear_greed

):


    score = 0

    detail = []



    # =====================
    # 데이터
    # =====================


    price = indicator.get(
        "price",
        0
    )


    ma20 = indicator.get(
        "MA20",
        0
    )


    ma20_trend = indicator.get(
        "MA20_TREND",
        ""
    )


    ma20_change = indicator.get(
        "MA20_CHANGE",
        ""
    )


    ma20_slope = indicator.get(
        "MA20_SLOPE",
        0
    )


    ma20_duration = indicator.get(
        "MA20_DURATION",
        0
    )



    # =====================
    # 1. MA20 추세 (20점)
    # =====================


    if ma20_trend == "📈 상승추세":


        score += 20


        detail.append(
            "📈 MA20 상승 추세 +20"
        )


    elif ma20_trend == "📉 하락추세":


        score += 0


        detail.append(
            "📉 MA20 하락 추세 +0"
        )


    else:


        score += 10


        detail.append(
            "➡️ MA20 횡보 +10"
        )



    # =====================
    # 2. MA20 추세 전환 (20점)
    # =====================


    if (
        "하락추세 → 📈 상승추세"
        in ma20_change
    ):


        score += 20


        detail.append(
            "🚀 MA20 상승 전환 발생 +20"
        )



    elif (
        "상승추세 → 📉 하락추세"
        in ma20_change
    ):


        score -= 10


        detail.append(
            "🚨 MA20 하락 전환 -10"
        )



    else:


        detail.append(
            "➡️ MA20 추세 유지"
        )



    # =====================
    # 3. MA20 Slope (10점)
    # =====================


    if ma20_slope >= 1:


        score += 10


        detail.append(
            "📈 MA20 강한 상승 기울기 +10"
        )



    elif ma20_slope > 0:


        score += 5


        detail.append(
            "📈 MA20 완만한 상승 +5"
        )



    elif ma20_slope < -1:


        score -= 5


        detail.append(
            "📉 MA20 강한 하락 -5"
        )



    else:


        detail.append(
            "➡️ MA20 기울기 약함"
        )



    # =====================
    # 4. MA20 유지 기간 (10점)
    # =====================


    if ma20_duration >= 20:


        score += 10


        detail.append(
            "🔥 MA20 추세 20일 이상 유지 +10"
        )


    elif ma20_duration >= 10:


        score += 7


        detail.append(
            "📈 MA20 추세 10일 이상 유지 +7"
        )


    elif ma20_duration >= 5:


        score += 3


        detail.append(
            "📊 MA20 추세 초기 유지 +3"
        )



    # =====================
    # 5. 가격 위치 (10점)
    # =====================


    if price > ma20:


        score += 10


        detail.append(
            "✅ 가격 20MA 위 +10"
        )


    else:


        score -= 5


        detail.append(
            "❌ 가격 20MA 아래 -5"
        )



    # =====================
    # 6. MACD (10점)
    # =====================


    if (

        indicator["MACD"]

        >

        indicator["MACD_SIGNAL"]

    ):


        score += 10


        detail.append(
            "📊 MACD 상승 +10"
        )


    else:


        detail.append(
            "📉 MACD 약세 +0"
        )



    # =====================
    # 7. RSI (5점)
    # =====================


    rsi = indicator["RSI"]


    if 40 <= rsi <= 70:


        score += 5


        detail.append(
            "✅ RSI 정상 +5"
        )


    elif rsi > 75:


        score -= 5


        detail.append(
            "⚠ RSI 과열 -5"
        )



    # =====================
    # 8. 거래량 (5점)
    # =====================


    if (

        indicator["Volume"]

        >=

        indicator["Volume_AVG"]

    ):


        score += 5


        detail.append(
            "📈 거래량 증가 +5"
        )



    # =====================
    # 9. 거시경제 (10점)
    # =====================


    macro = min(

        max(

            macro_score,

            0

        ),

        10

    )


    score += macro


    detail.append(
        f"🌎 거시경제 +{macro}"
    )



    # =====================
    # 10. 시장심리 (10점)
    # =====================


    if 40 <= fear_greed <= 70:


        score += 10


        detail.append(
            "😊 시장심리 안정 +10"
        )


    elif fear_greed < 40:


        score += 5


        detail.append(
            "😨 공포 구간 +5"
        )


    else:


        score -= 5


        detail.append(
            "⚠ 과열 구간 -5"
        )



    # =====================
    # 점수 보정
    # =====================


    if score > 100:

        score = 100



    if score < 0:

        score = 0



    return score, detail





# =====================
# 등급
# =====================

def get_grade(score):


    if score >= 90:

        return "⭐ 강력 매수"



    elif score >= 80:

        return "🟢 적극 매수"



    elif score >= 70:

        return "🟢 매수"



    elif score >= 60:

        return "🟡 분할매수"



    elif score >= 50:

        return "🟠 관망"



    else:

        return "🔴 비중축소"
