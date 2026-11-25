def calculate_score(
    indicator,
    vix,
    rate,
    dxy
):

    score = 0

    detail = []


    # ======================
    # 기술적 분석 60점
    # ======================


    # 현재가 > 20일선
    if indicator["price"] > indicator["MA20"]:

        score += 15

        detail.append(
            "✅ 현재가 > 20일선 +15"
        )


    else:

        detail.append(
            "❌ 현재가 < 20일선 +0"
        )



    # 5일선 > 20일선

    if indicator["MA5"] > indicator["MA20"]:

        score += 15

        detail.append(
            "✅ 5일선 > 20일선 +15"
        )



    else:

        detail.append(
            "❌ 5일선 약세 +0"
        )



    # 20일선 > 60일선

    if indicator["MA20"] > indicator["MA60"]:

        score += 10

        detail.append(
            "✅ 중기 상승추세 +10"
        )


    else:

        detail.append(
            "❌ 중기 약세 +0"
        )



    # RSI

    if 40 <= indicator["RSI"] <= 70:

        score += 10

        detail.append(
            "✅ RSI 정상 +10"
        )


    else:

        detail.append(
            "⚠ RSI 주의 +0"
        )



    # MACD

    if indicator["MACD"] > indicator["MACD_SIGNAL"]:

        score += 10

        detail.append(
            "✅ MACD 상승 +10"
        )


    else:

        detail.append(
            "❌ MACD 약세 +0"
        )



    # ======================
    # 거래량 10점
    # ======================


    if indicator["Volume"] > indicator["Volume_AVG"]:

        score += 10

        detail.append(
            "✅ 거래량 증가 +10"
        )



    # ======================
    # 거시경제 30점
    # ======================


    # VIX

    if vix < 20:

        score += 10

        detail.append(
            "✅ VIX 안정 +10"
        )


    elif vix < 30:

        score += 5

        detail.append(
            "⚠ VIX 보통 +5"
        )


    else:

        detail.append(
            "❌ 공포구간 +0"
        )



    # 금리

    if rate < 4.5:

        score += 10

        detail.append(
            "✅ 금리 부담 낮음 +10"
        )


    else:

        detail.append(
            "⚠ 금리 부담 +0"
        )



    # 달러

    if dxy < 105:

        score += 10

        detail.append(
            "✅ 달러 안정 +10"
        )


    else:

        detail.append(
            "⚠ 달러 강세 +0"
        )



    return score, detail



# ======================
# 투자 등급
# ======================

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


    elif score >= 40:

        return "🔴 비중축소"


    else:

        return "⚫ 매도 검토"
