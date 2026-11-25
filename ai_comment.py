import os

from openai import OpenAI



def create_comment(

    score,

    grade,

    indicator,

    vix,

    rate,

    dxy,

    macro_detail

):


    # ==========================
    # OpenAI API Key 확인
    # ==========================

    api_key = os.getenv(
        "OPENAI_API_KEY"
    )


    if not api_key:

        return create_default_comment(

            score,

            grade,

            vix,

            rate,

            dxy

        )



    try:


        client = OpenAI(

            api_key=api_key

        )



        prompt = f"""

당신은 미국 ETF 전문 투자 애널리스트입니다.

QQQ 투자 리포트를 작성하세요.


[시장 데이터]


QQQ 현재가격:
{indicator.get("price")}


투자점수:
{score}/100


투자등급:
{grade}


VIX:
{vix}


미국 10년물 금리:
{rate}


달러지수:
{dxy}



[거시경제 평가]

{macro_detail}



아래 내용을 포함하세요.


1. 현재 시장 상황

2. 기술적 분석

3. 거시경제 위험요인

4. 투자 전략


마지막 줄에는 반드시 작성:


투자 판단:
(적극매수 / 분할매수 / 보유 / 비중축소 / 매도)



전문 투자보고서 스타일로

5~8문장 작성하세요.

"""



        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {

                    "role": "system",

                    "content":
                    "당신은 월스트리트 투자 분석가입니다."

                },

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            temperature=0.3

        )



        return response.choices[0].message.content



    except Exception as e:


        print()

        print(
            "AI 분석 실패:",
            e
        )


        return create_default_comment(

            score,

            grade,

            vix,

            rate,

            dxy

        )





def create_default_comment(

    score,

    grade,

    vix,

    rate,

    dxy

):


    if score >= 70:

        action = "분할매수"

    elif score >= 50:

        action = "보유"

    elif score >= 30:

        action = "비중축소"

    else:

        action = "매도 검토"



    return f"""

QQQ AI 투자 분석


현재 투자점수는 {score}/100점이며,

투자등급은 {grade} 입니다.


기술적 지표와 거시경제 환경을 종합하면

현재 시장 위험도를 확인하면서

신중한 투자 접근이 필요한 구간입니다.


VIX 지수:
{vix}


미국 10년물 금리:
{rate}


달러지수:
{dxy}


단기적으로 변동성이 확대될 가능성이 있어

추격 매수보다는 시장 방향성을 확인하는 전략이 적절합니다.


투자 판단:
{action}

"""
