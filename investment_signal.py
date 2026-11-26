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



    price = indicator.get(
        "price",
        0
    )


    ma20 = indicator.get(
        "ma20",
        0
    )


    ma20_prev = indicator.get(
        "ma20_prev",
        0
    )



    # =========================
    # 20일 이동평균 추세 판단
    # =========================

    if ma20 > 0 and ma20_prev > 0:


        if ma20 > ma20_prev:


            ma20_trend = "📈 상승추세"


            buy_score += 1


            reasons.append(
                "20일 이동평균선 상승추세"
            )



        elif ma20 < ma20_prev:


            ma20_trend = "📉 하락추세"


            sell_score += 1


            reasons.append(
                "20일 이동평균선 하락추세"
            )



        else:


            ma20_trend = "➡️ 횡보"


            reasons.append(
                "20일 이동평균선 횡보"
            )


    else:


        ma20_trend = "데이터 부족"



    # =========================
    # 매수 판단
    # =========================


    if score >= 70:


        buy_score += 1


        reasons.append(
            "투자점수 우수 (70점 이상)"
        )



    elif score < 30:


        sell_score += 1


        reasons.append(
            "투자점수 위험 구간"
        )



    # =========================
    # 가격 vs 20MA
    # =========================


    if ma20 > 0 and price > ma20:


        buy_score += 1


        reasons.append(
            "QQQ 가격이 20일 이동평균 위"
        )



    elif ma20 > 0 and price < ma20:


        sell_score += 1


        reasons.append(
            "QQQ 가격이 20일 이동평균 아래"
        )



    # =========================
    # VIX 판단
    # =========================


    if vix < 20:


        buy_score += 1


        reasons.append(
            "VIX 안정 구간"
        )



    elif vix > 30:


        sell_score += 1


        reasons.append(
            "VIX 위험 수준"
        )


    else:


        reasons.append(
            "VIX 중립 구간"
        )



    # =========================
    # 공포탐욕지수 판단
    # =========================


    if fear_greed < 30:


        buy_score += 1


        reasons.append(
            "공포 구간 분할매수 기회"
        )


    elif fear_greed > 80:


        sell_score += 1


        reasons.append(
            "탐욕 과열 구간"
        )



    # =========================
    # 금리 판단
    # =========================


    if rate:


        reasons.append(
            f"금리 지표 확인: {rate}"
        )



    # =========================
    # 최종 투자 신호
    # =========================


    if buy_score >= 3:


        signal = "🟢 매수 검토"


        action = (
            "중기 상승추세 확인, "
            "분할 매수 접근 검토"
        )



    elif sell_score >= 2:


        signal = "🔴 위험 관리"


        action = (
            "20일선 추세 약화, "
            "비중 축소 및 현금 관리"
        )



    else:


        signal = "🟡 보유"


        action = (
            "추세 확인 후 대응"
        )



    return {


        "signal":
        signal,


        "action":
        action,


        "reason":
        reasons,


        "ma20_trend":
        ma20_trend,


        "ma20":
        ma20,


        "ma20_prev":
        ma20_prev,


        "buy_score":
        buy_score,


        "sell_score":
        sell_score

    }
