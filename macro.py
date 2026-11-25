import requests


# ==========================
# VIX 평가
# ==========================

def vix_score(vix):

    if vix < 15:

        return 8, "VIX 매우 안정"


    elif vix < 20:

        return 10, "VIX 안정"


    elif vix < 30:

        return 7, "VIX 주의"


    else:

        return 3, "공포 구간"



# ==========================
# 금리 평가
# ==========================

def rate_score(current, previous):

    if current < previous:

        return 10, "금리 하락 (긍정)"


    elif current <= previous + 0.05:

        return 7, "금리 안정"


    else:

        return 3, "금리 상승 부담"



# ==========================
# 달러 평가
# ==========================

def dxy_score(current, previous):

    if current < previous:

        return 10, "달러 약세 (긍정)"


    elif current <= previous + 0.2:

        return 7, "달러 안정"


    else:

        return 3, "달러 강세 부담"



# ==========================
# Fear & Greed
# ==========================

def get_fear_greed():


    try:

        url = (
            "https://api.alternative.me/"
            "fng/?limit=1"
        )


        data = requests.get(
            url,
            timeout=10
        ).json()


        value = int(
            data["data"][0]["value"]
        )


        return value


    except:

        return 50



def fear_greed_score(value):


    if 45 <= value <= 70:

        return 10, "시장 심리 양호"


    elif value < 45:

        return 7, "공포 구간"


    else:

        return 5, "탐욕 구간"



# ==========================
# 종합 거시 점수
# ==========================

def calculate_macro_score(
        vix,
        rate,
        rate_prev,
        dxy,
        dxy_prev
):


    total = 0

    detail = []


    score, text = vix_score(vix)

    total += score

    detail.append(
        f"VIX : {text} +{score}"
    )



    score, text = rate_score(
        rate,
        rate_prev
    )

    total += score

    detail.append(
        f"금리 : {text} +{score}"
    )



    score, text = dxy_score(
        dxy,
        dxy_prev
    )

    total += score

    detail.append(
        f"DXY : {text} +{score}"
    )



    fg = get_fear_greed()


    score, text = fear_greed_score(
        fg
    )


    total += score


    detail.append(
        f"Fear&Greed : {fg} ({text}) +{score}"
    )


    return total, detail
