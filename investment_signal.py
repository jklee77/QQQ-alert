def get_investment_signal(

    score,

    indicator,

    vix,

    rate,

    fear_greed

):


    reasons = []

    buy_score = 0

    sell_score = 0



    # =========================
    # 데이터
    # =========================


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


    macd = indicator.get(
        "MACD",
        0
    )


    macd_signal = indicator.get(
        "MACD_SIGNAL",
        0
    )



    # =========================
    # MA20 추세 전환 분석
    # =========================


    if "하락추세 → 📈 상승추세" in ma20_change:


        buy_score += 3


        reasons.append(
            "🚀 20일 이동평균 상승 추세 전환 발생"
        )



    elif "상승추세 → 📉 하락추세" in ma20_change:


        sell_score += 3


        reasons.append(
            "⚠️ 20일 이동평균 하락 추세 전환 발생"
        )



    # =========================
    # 현재 MA20 위치
    # =========================


    if price > ma20:


        buy_score += 1


        reasons.append(
            "✅ 가격이 20일 이동평균 위"
        )


    else:


        sell_score += 1


        reasons.append(
            "❌ 가격이 20일 이동평균 아래"
        )



    # =========================
    # MA20 방향
    # =========================


    if ma20_trend == "📈 상승추세":


        buy_score += 1


        reasons.append(
            "📈 20일 이동평균 상승 방향"
        )


    elif ma20_trend == "📉 하락추세":


        sell_score += 1


        reasons.append(
            "📉 20일 이동평균 하락 방향"
        )



    # =========================
    # MACD
    # =========================


    if macd > macd_signal:


        buy_score += 1


        reasons.append(
            "📊 MACD 상승 신호"
        )


    else:


        sell_score += 1


        reasons.append(
            "📉 MACD 약세"
        )



    # =========================
    # VIX
    # =========================


    if vix < 20:


        buy_score += 1


        reasons.append(
            "😌 VIX 안정 구간"
        )


    elif vix > 30:


        sell_score += 1


        reasons.append(
            "🚨 VIX 위험 구간"
        )



    # =========================
    # 투자점수 보조
    # =========================


    if score >= 70:


        buy_score += 1


        reasons.append(
            "⭐ 종합 투자점수 우수"
        )


    elif score < 50:


        sell_score += 1


        reasons.append(
            "⚠️ 종합 투자점수 약세"
        )



    # =========================
    # 최종 판단
    # =========================


    if buy_score >= 4:


        signal = (
            "🟢 MA20 상승 추세 매수 검토"
        )


        action = (

            "분할 매수 접근\n"
            "상승 추세 유지 여부 확인"

        )



    elif sell_score >= 3:


        signal = (
            "🔴 MA20 추세 위험 관리"
        )


        action = (

            "비중 축소 검토\n"
            "MA20 회복 여부 확인"

        )



    else:


        signal = (
            "🟡 MA20 추세 관찰"
        )


        action = (

            "보유 유지\n"
            "추가 방향 확인"

        )



    return {


        "signal":
        signal,


        "action":
        action,


        "reason":
        reasons,


        "buy_score":
        buy_score,


        "sell_score":
        sell_score

    }
