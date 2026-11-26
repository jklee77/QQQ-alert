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



    # =========================
    # 매수 판단
    # =========================

    if score >= 70:

        buy_score += 1

        reasons.append(
            "투자점수 우수 (70점 이상)"
        )



    if ma20 > 0 and price > ma20:

        buy_score += 1

        reasons.append(
            "QQQ 가격이 20일 이동평균 위"
        )


    else:

        reasons.append(
            "QQQ 가격이 20일 이동평균 아래"
        )



    if vix < 20:

        buy_score += 1

        reasons.append(
            "VIX 안정 구간"
        )


    else:

        reasons.append(
            "VIX 변동성 확대 구간"
        )



    if fear_greed < 30:

        buy_score += 1

        reasons.append(
            "공포 구간 분할매수 검토 가능"
        )



    # =========================
    # 매도 위험 판단
    # =========================

    if score < 30:

        sell_score += 1

        reasons.append(
            "투자점수 위험 구간"
        )



    if ma20 > 0 and price < ma20:

        sell_score += 1

        reasons.append(
            "20일 이동평균 하회"
        )



    if vix > 30:

        sell_score += 1

        reasons.append(
            "VIX 위험 수준"
        )



    # =========================
    # 최종 신호
    # =========================

    if buy_score >= 3:


        signal = "🟢 매수 검토"


        action = (
            "분할 매수 접근 검토"
        )



    elif sell_score >= 2:


        signal = "🔴 위험 관리"


        action = (
            "비중 축소 검토"
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
        reasons

    }
