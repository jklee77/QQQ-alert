def calculate_final_score(

    indicator,

    macro_score,

    fear_greed

):


    score = 50

    detail = []



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



    # =====================
    # 1. MA20 추세 분석
    # =====================


    if ma20_trend == "📈 상승추세":


        score += 15


        detail.append(
            "📈 MA20 상승 추세 +15"
        )



    elif ma20_trend == "📉 하락추세":


        score -= 10


        detail.append(
            "📉 MA20 하락 추세 -10"
        )



    # 추세 전환

    if (
        "하락추세 → 📈 상승추세"
        in ma20_change
    ):


        score += 20


        detail.append(
            "🚀 MA20 상승 전환 +20"
        )



    elif (
        "상승추세 → 📉 하락추세"
        in ma20_change
    ):


        score -= 20


        detail.append(
            "🚨 MA20 하락 전환 -20"
        )



    # 가격 위치

    if price > ma20:


        score += 15


        detail.append(
            "✅ 가격 MA20 위 +15"
        )


    else:


        score -= 10


        detail.append(
            "❌ 가격 MA20 아래 -10"
        )



    # =====================
    # 2. 기술 보조지표
    # =====================


    if indicator["MACD"] > indicator["MACD_SIGNAL"]:


        score += 10


        detail.append(
            "📊 MACD 상승 +10"
        )


    else:


        score -= 5


        detail.append(
            "📉 MACD 약세 -5"
        )



    if 40 <= indicator["RSI"] <= 70:


        score += 5


        detail.append(
            "✅ RSI 정상 +5"
        )


    elif indicator["RSI"] > 75:


        score -= 5


        detail.append(
            "⚠ RSI 과열 -5"
        )



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
    # 3. 거시경제
    # =====================


    macro = min(
        max(
            macro_score,
            0
        ),
        20
    )


    score += macro


    detail.append(
        f"🌎 거시경제 +{macro}"
    )



    # =====================
    # 4. 시장 심리
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
    # 점수 제한
    # =====================


    if score > 100:

        score = 100


    if score < 0:

        score = 0



    return score, detail





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
