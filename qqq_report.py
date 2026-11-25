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

from score_history import (
    get_previous_score,
    save_score,
    score_change_report
)

from chart import (
    create_qqq_chart
)

# 중요: signal.py 충돌 방지
from investment_signal import (
    get_investment_signal
)



def main():

    print("==============================")
    print("QQQ AI 투자 리포트 시작")
    print("==============================")


    # =========================
    # 데이터 수집
    # =========================

    qqq = get_qqq()

    vix_data = get_vix()

    dxy_data = get_dxy()

    rate_data = get_us10y()



    # =========================
    # 기술적 분석
    # =========================

    qqq = calculate_indicators(
        qqq
    )


    indicator = get_indicator_summary(
        qqq
    )



    # =========================
    # 시장 데이터
    # =========================

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



    # =========================
    # Fear & Greed
    # =========================

    fear_greed = get_fear_greed()



    # =========================
    # 거시경제 분석
    # =========================

    macro_score, macro_detail = calculate_macro_score(

        vix,

        rate,

        rate_prev,

        dxy,

        dxy_prev

    )



    # =========================
    # 투자 점수
    # =========================

    score, detail = calculate_final_score(

        indicator,

        macro_score,

        fear_greed

    )


    grade = get_grade(
        score
    )



    # =========================
    # 전일 점수 비교
    # =========================

    previous_score = get_previous_score()


    change_report = score_change_report(

        score,

        previous_score

    )


    save_score(
        score
    )



    # =========================
    # 투자 행동 신호
    # =========================

    investment_signal = get_investment_signal(

        score,

        indicator,

        vix,

        rate,

        fear_greed

    )



    # =========================
    # 차트 생성
    # =========================

    chart_file = create_qqq_chart(
        qqq
    )



    # =========================
    # AI 의견
    # =========================

    comment = create_comment(

        score,

        grade,

        indicator,

        vix,

        rate,

        dxy,

        macro_detail

    )



    # =========================
    # 콘솔 출력
    # =========================

    print()

    print("==============================")
    print("QQQ AI 투자 리포트")
    print("==============================")


    print(
        "현재 가격:",
        indicator["price"]
    )


    print(
        "투자 점수:",
        score,
        "/100"
    )


    print(
        "투자 등급:",
        grade
    )


    print(
        "투자 신호:",
        investment_signal["signal"]
    )


    print()

    print("[AI 투자 의견]")

    print(comment)



    print()

    print("[기술적 평가]")

    for item in detail:

        print(item)



    print()

    print("[거시경제 평가]")

    for item in macro_detail:

        print(item)



    # =========================
    # HTML 리포트 생성
    # =========================

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

<hr>

<h2>
📊 전일 대비 투자점수 변화
</h2>

<p>
현재 점수:
<b>{score}/100</b>
</p>

<p>
{change_report}
</p>


<hr>


<h2>
📌 투자 행동 신호
</h2>


<h3>
{investment_signal["signal"]}
</h3>


<p>
<b>추천 행동</b><br>
{investment_signal["action"]}
</p>


<p>
<b>판단 근거</b>
</p>

<ul>

"""


    for reason in investment_signal["reason"]:

        html += f"""

<li>
{reason}
</li>

"""


    html += """

</ul>


<hr>


<h2>
📈 QQQ 기술 분석 차트
</h2>


<img src="cid:qqq_chart">


<hr>


<h2>
🤖 AI 투자 의견
</h2>


<p>
"""


    html += comment


    html += """

</p>

"""



    # =========================
    # 이메일 발송
    # =========================

    try:

        send_email(

            html,

            chart_file

        )


        print()

        print(
            "메일 발송 성공"
        )


    except Exception as e:

        print()

        print(
            "메일 발송 실패:",
            e
        )

        raise



    print()

    print(
        "QQQ 리포트 완료"
    )



if __name__ == "__main__":

    main()
