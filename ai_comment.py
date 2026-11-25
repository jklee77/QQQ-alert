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

    client = OpenAI(
        api_key=os.environ.get(
            "OPENAI_API_KEY"
        )
    )


    prompt = f"""
당신은 미국 ETF 전문 투자 애널리스트입니다.

QQQ 투자 분석 리포트를 작성하세요.

[현재 투자 데이터]

QQQ 현재 가격:
{indicator.get("price")}

투자 점수:
{score}/100

투자 등급:
{grade}

VIX:
{vix}

미국 10년물 금리:
{rate}

달러 인덱스:
{dxy}


[거시경제 평가]

{macro_detail}


다음 내용을 포함하여 작성하세요.

1. 현재 시장 상황 요약
2. 기술적 분석 평가
3. 거시경제 위험 요인
4. 투자 전략 제안

마지막에는 반드시 아래 형식으로 결론을 작성하세요.

투자 판단:
- 적극매수 / 분할매수 / 보유 / 비중축소 / 매도

투자 의견은 5~8문장으로 작성하고,
전문 투자 리포트처럼 작성하세요.
"""


    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content":
                "당신은 월스트리트 투자 애널리스트입니다."
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.3

    )


    return response.choices[0].message.content
