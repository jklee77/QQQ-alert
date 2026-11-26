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


from investment_signal import (
    get_investment_signal
)




def get_mail_subject(indicator):


    change = indicator.get(
        "MA20_CHANGE",
        ""
    )



    if (

        "📉 하락추세 → 📈 상승추세"

        in change

    ):


        return (
            "🚨 QQQ MA20 상승 추세 전환 알림"
        )



    elif (

        "📈 상승추세 → 📉 하락추세"

        in change

    ):


        return (
            "🚨 QQQ MA20 하락 추세 전환 알림"
        )



    else:


        return (
            "📈 QQQ AI 투자 리포트"
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
    # 기술 분석
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
    # Fear Greed
    # =========================


    fear_greed = get_fear_greed()




    # =========================
    # 거시경제
    # =========================


    macro_score, macro_detail = calculate_macro_score(

        vix,

        rate,

        rate_prev,

        dxy,

        dxy_prev

    )




    # =========================
    # 점수
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
    # 점수 비교
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
    # 투자 신호
    # =========================


    investment_signal = get_investment_signal(

        score,

        indicator,

        vix,

        rate,

        fear_greed

    )




    # =========================
    # 차트
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
    # HTML
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
📌 MA20 투자 신호
</h2>


<h3>
{investment_signal["signal"]}
</h3>


<p>
{investment_signal["action"]}
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
📊 투자 점수 변화
</h2>

"""



    html += f"""

<p>
{change_report}
</p>


<hr>

<h2>
🤖 AI 의견
</h2>


<p>
{comment}
</p>


<hr>


<img src="cid:qqq_chart">


"""



    # =========================
    # 이메일 제목 결정
    # =========================


    subject = get_mail_subject(
        indicator
    )



    print()

    print(
        "메일 제목:",
        subject
    )




    # =========================
    # 이메일 발송
    # =========================


    send_email(

        html,

        chart_file,

        subject

    )



    print()

    print(
        "QQQ 리포트 완료"
    )




if __name__ == "__main__":

    main()
