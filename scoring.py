def calculate_final_score(
    indicator,
    macro_score,
    fear_greed
):

    score = 0

    detail = []


    # =====================
    # 기술적 분석 50점
    # =====================


    if indicator["price"] > indicator["MA20"]:

        score += 15

        detail.append(
            "✅ 가격 20일선 위 +15"
        )


    if indicator["MA5"] > indicator["MA20"]:

        score += 15

        detail.append(
            "✅ 단기 상승추세 +15"
        )


    if indicator["MA20"] > indicator["MA60"]:

        score += 10

        detail.append(
            "✅ 중기 상승추세 +10"
        )


    if 40 <= indicator["RSI"] <= 70:

        score += 5

        detail.append(
            "✅ RSI 정상 +5"
        )


    if indicator["MACD"] > indicator["MACD_SIGNAL"]:

        score += 5

        detail.append(
            "✅ MACD 상승 +5"
        )


    # =====================
    # 거시경제 30점
    # =====================


    macro = min(
        macro_score,
        30
    )

    score += macro


    detail.append(
        f"🌎 거시경제 +{macro}"
    )


    # =====================
    # 시장 심리 10점
    # =====================


    if 40 <= fear_greed <= 70:

        score += 10

        detail.append(
            "😊 시장심리 안정 +10"
        )


    elif fear_greed < 40:

        score += 7

        detail.append(
            "😨 공포구간 +7"
        )


    else:

        score += 5

        detail.append(
            "⚠ 과열주의 +5"
        )


    # =====================
    # 위험관리 10점
    # =====================


    if indicator["Volume"] >= indicator["Volume_AVG"]:

        score += 5

        detail.append(
            "📈 거래량 확인 +5"
        )


    if indicator["RSI"] < 75:

        score += 5

        detail.append(
            "🛡 과매수 위험 낮음 +5"
        )


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
