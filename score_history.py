import json

import os

from datetime import datetime




FILE_NAME = "score_history.json"





# =========================
# 기록 파일 생성
# =========================

def load_history():


    if not os.path.exists(FILE_NAME):


        return []



    try:


        with open(

            FILE_NAME,

            "r",

            encoding="utf-8"

        ) as f:


            return json.load(f)



    except:


        return []






# =========================
# 전일 점수 조회
# =========================

def get_previous_score():


    history = load_history()



    if len(history) == 0:


        return None



    return history[-1]["score"]






# =========================
# 점수 저장
# =========================

def save_score(score):


    history = load_history()



    data = {


        "date":

            datetime.now()
            .strftime(
                "%Y-%m-%d"
            ),


        "score":

            score


    }



    history.append(
        data
    )



    with open(

        FILE_NAME,

        "w",

        encoding="utf-8"

    ) as f:



        json.dump(

            history,

            f,

            indent=4,

            ensure_ascii=False

        )






# =========================
# MA20 기록 저장
# =========================

def save_ma20_history(

    indicator,

    score,

    signal

):


    history = load_history()



    data = {


        "date":

            datetime.now()
            .strftime(
                "%Y-%m-%d"
            ),



        "price":

            indicator.get(
                "price",
                0
            ),



        "score":

            score,



        "MA20_TREND":

            indicator.get(
                "MA20_TREND",
                ""
            ),



        "MA20_CHANGE":

            indicator.get(
                "MA20_CHANGE",
                ""
            ),



        "MA20_SLOPE":

            indicator.get(
                "MA20_SLOPE",
                0
            ),



        "MA20_DURATION":

            indicator.get(
                "MA20_DURATION",
                0
            ),



        "SIGNAL":

            signal.get(
                "signal",
                ""
            )


    }



    history.append(
        data
    )



    with open(

        FILE_NAME,

        "w",

        encoding="utf-8"

    ) as f:



        json.dump(

            history,

            f,

            indent=4,

            ensure_ascii=False

        )







# =========================
# 점수 변화 분석
# =========================

def score_change_report(

    current_score,

    previous_score

):



    if previous_score is None:


        return (
            "첫 번째 리포트입니다."
        )




    diff = (

        current_score

        -

        previous_score

    )




    if diff > 0:



        return (

            f"📈 전일 대비 "

            f"+{diff}점 상승"

        )



    elif diff < 0:



        return (

            f"📉 전일 대비 "

            f"{diff}점 하락"

        )



    else:



        return (

            "➡️ 전일 대비 변화 없음"

        )
