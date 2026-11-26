from datetime import datetime



def create_report(

    indicator,

    score,

    grade,

    detail,

    vix,

    rate,

    dxy

):


    today = datetime.now().strftime(
        "%Y-%m-%d"
    )



    detail_text = "<br>".join(
        detail
    )



    html = f"""

<html>

<body>


<h2>
📈 QQQ AI 투자 리포트
</h2>



<p>
날짜 : {today}
</p>



<hr>



<h2>
⭐ 종합 투자 점수
</h2>



<h1>
{score} / 100
</h1>



<h2>
{grade}
</h2>



<hr>



<h3>
📊 QQQ 기술 분석
</h3>



<table border="1"
cellpadding="5">



<tr>
<td>현재가격</td>
<td>${indicator["price"]}</td>
</tr>



<tr>
<td>5일 이동평균</td>
<td>{indicator["MA5"]}</td>
</tr>



<tr>
<td>20일 이동평균</td>
<td>{indicator["MA20"]}</td>
</tr>



<tr>
<td>5일 전 20일 이동평균</td>
<td>{indicator["MA20_PREV"]}</td>
</tr>



<tr>
<td>20일 이동평균 추세</td>
<td>
{indicator["MA20_TREND"]}
</td>
</tr>



<tr>
<td>가격 위치</td>
<td>
{indicator["PRICE_VS_MA20"]}
</td>
</tr>



<tr>
<td>60일 이동평균</td>
<td>{indicator["MA60"]}</td>
</tr>



<tr>
<td>120일 이동평균</td>
<td>{indicator["MA120"]}</td>
</tr>



<tr>
<td>RSI</td>
<td>{indicator["RSI"]}</td>
</tr>



<tr>
<td>MACD</td>
<td>{indicator["MACD"]}</td>
</tr>



<tr>
<td>MACD Signal</td>
<td>{indicator["MACD_SIGNAL"]}</td>
</tr>



</table>




<hr>



<h3>
🌎 거시경제
</h3>



<p>


VIX :
{vix}


<br><br>


미국 10년물 금리 :
{rate}


<br><br>


달러지수 :
{dxy}


</p>




<hr>




<h3>
📌 점수 상세 평가
</h3>



<p>

{detail_text}

</p>




<hr>




<h3>
🤖 AI 투자 판단 기준
</h3>


<p>


20일 이동평균선 기준:
<br>


{indicator["MA20_TREND"]}


<br><br>


현재 가격 위치:
<br>


{indicator["PRICE_VS_MA20"]}


</p>




<hr>




<p>

본 리포트는 투자 참고용 분석 자료이며,
투자 결정은 개인의 판단과 책임 하에 이루어져야 합니다.

</p>



</body>

</html>

"""


    return html
