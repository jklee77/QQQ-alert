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
    calculate_final_score,
    get_grade
)

from macro import (
    calculate_macro_score,
    get_fear_greed
)

from ai_comment import (
    create_comment
)

from report import (
    create_report
)

from mail import (
    send_email
)



def main():


    print("==============================")
    print("QQQ AI 투자 리포트 시작")
    print("==============================")


    # =================================
    # 데이터 수집
    # =================================


    qqq = get_qqq()

    vix_data = get_vix()

    dxy_data = get_dxy()

    rate_data = get_us10y()



    # =================================
    # 기술 지표 계산
    # =================================


    qqq = calculate_indicators(
        qqq
    )


    indicator = get_indicator_summary(
        qqq
    )



    # =================================
    # 현재 시장 데이터
    # =================================


    vix = float(
        vix_data["Close"].iloc[-1]
    )


    rate = float(
        rate_data["Close"].iloc[-1]
    )


    rate_prev = float(
        rate_data["Close"].iloc[-2]
    )


    dxy = float(
        dxy_data["Close"].iloc[-1]
    )


    dxy_prev = float(
        dxy_data["Close"].iloc[-2]
    )



    # =================================
    # Fear & Greed
    # =================================


    fear_greed = get_fear_greed()



    # =================================
    # 거시경제 점수
    # =================================


    macro_score, macro_detail = calculate_macro_score(

        vix,

        rate,

        rate_prev,

        dxy,

        dxy_prev

    )



    # =================================
    # 최종 투자 점수
    # =================================


    score, detail = calculate_final_score(

        indicator,

        macro_score,

        fear_greed

    )



    grade = get_grade(
        score
    )



    # =================================
    # AI 의견
    # =================================


    comment = create_comment(

        score,

        grade

    )



    # =================================
    # 콘솔 출력
    # =================================


    print(
f"""

================================

QQQ AI 투자 리포트


현재 가격 :
${indicator["price"]}



투자 점수 :

{score} / 100


투자 등급 :

{grade}



기술 분석

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



거시경제


VIX :
{vix}


미국10년물 금리 :
{rate}


달러지수 :
{dxy}


Fear & Greed :
{fear_greed}



AI 의견

{comment}


================================

"""
    )



    print("\n[상세 평가]")


    for item in detail:

        print(item)



    print("\n[거시경제 평가]")


    for item in macro_detail:

        print(item)



    # =================================
    # 이메일 HTML 생성
    # =================================


    html = create_report(

        indicator,

        score,

        grade,

        detail,

        vix,

        rate,

        dxy

    )



    html += f"""

<h3>
AI 투자 의견
</h3>

<p>

{comment}

</p>

"""



    # =================================
    # 이메일 발송
    # =================================


     try:

        send_email(html)


    except Exception as e:

        print(
            "메일 발송 실패:",
            e
        )


    print(
        "QQQ 리포트 완료"
    )
