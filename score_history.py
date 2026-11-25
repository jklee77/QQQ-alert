import json
import os
from datetime import datetime


FILE = "score_history.json"


def get_previous_score():

    if not os.path.exists(FILE):
        return None

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data.get("score")

    except:
        return None



def save_score(score):

    data = {

        "date":
        datetime.now().strftime("%Y-%m-%d"),

        "score":
        score

    }


    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def score_change_report(
    today,
    previous
):

    if previous is None:

        return "첫 번째 분석 데이터입니다."


    diff = today - previous


    if diff > 0:

        return (
            f"전일 대비 투자점수 +{diff}점 상승\n"
            "시장 환경이 개선되고 있습니다."
        )


    elif diff < 0:

        return (
            f"전일 대비 투자점수 {diff}점 하락\n"
            "위험요인 증가를 확인해야 합니다."
        )


    else:

        return (
            "전일 대비 투자점수 변화 없음"
        )
