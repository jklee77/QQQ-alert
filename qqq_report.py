from report import create_report
from mail import send_email
from data_loader import (
    get_qqq,
    get_vix,
    get_dxy,
    get_us10y
)

from indicators import (
    calculate_indicators,
    get_indicator_summary
)

from scoring import (
    calculate_score,
    get_grade
)


def main():

    print("==========================")
    print("QQQ AI 투자 리포트")
    print("==========================")


    # 데이터 수집

    qqq = get_qqq()

    vix = get_vix()

    dxy = get_dxy()

    us10y = get_us10y()



    # 기술 지표 계산

    qqq = calculate_indicators(qqq)

    indicator = get_indicator_summary(qqq)



    # 거시경제 값

    vix_price = float(
        vix["Close"].iloc[-1]
    )


    dxy_price = float(
        dxy["Close"].iloc[-1]
    )


    rate = float(
        us10y["Close"].iloc[-1]
    )



    # 투자 점수 계산

    score, detail = calculate_score(
        indicator,
        vix_price,
        rate,
        dxy_price
    )


    grade = get_grade(score)



    # 리포트 출력

    print(
f"""

━━━━━━━━━━━━━━━━━━

QQQ 현재가

${indicator["price"]}


기술적 분석

5일선 :
{indicator["MA5"]}

20일선 :
{indicator["MA20"]}

60일선 :
{indicator["MA60"]}

120일선 :
{indicator["MA120"]}


RSI :
{indicator["RSI"]}


MACD :
{indicator["MACD"]}


━━━━━━━━━━━━━━━━━━

거시경제

VIX :
{vix_price}

미국10년물 금리 :
{rate}

달러지수 :
{dxy_price}



━━━━━━━━━━━━━━━━━━

투자 평가


종합 점수 :

{score} / 100


투자 등급 :

{grade}


━━━━━━━━━━━━━━━━━━

"""
    )


    for item in detail:
        print(item)


    html = create_report(
        indicator,
        score,
        grade,
        detail,
        vix_price,
        rate,
        dxy_price
    )


    send_email(html)
