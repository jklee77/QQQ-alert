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


def main():

    print("==========================")
    print("QQQ AI 투자 리포트")
    print("==========================")


    # =====================
    # 데이터 수집
    # =====================

    qqq = get_qqq()

    vix = get_vix()

    dxy = get_dxy()

    us10y = get_us10y()



    # =====================
    # 기술적 지표 계산
    # =====================

    qqq = calculate_indicators(qqq)

    indicator = get_indicator_summary(qqq)



    # =====================
    # 거시경제 데이터
    # =====================

    qqq_price = indicator["price"]

    vix_price = float(
        vix["Close"].iloc[-1]
    )

    dxy_price = float(
        dxy["Close"].iloc[-1]
    )

    rate = float(
        us10y["Close"].iloc[-1]
    )



    # =====================
    # 출력
    # =====================

    print(
f"""

QQQ 현재가
${qqq_price}


━━━━━━━━━━━━━━━━
기술적 분석
━━━━━━━━━━━━━━━━


5일 이동평균
{indicator["MA5"]}


20일 이동평균
{indicator["MA20"]}


60일 이동평균
{indicator["MA60"]}


120일 이동평균
{indicator["MA120"]}


RSI
{indicator["RSI"]}


MACD
{indicator["MACD"]}


MACD Signal
{indicator["MACD_SIGNAL"]}


거래량
{indicator["Volume"]:,}


20일 평균 거래량
{indicator["Volume_AVG"]:,}



━━━━━━━━━━━━━━━━
거시경제
━━━━━━━━━━━━━━━━


VIX
{vix_price}


달러지수(DXY)
{dxy_price}


미국 10년물 금리
{rate}



━━━━━━━━━━━━━━━━

데이터 수집 및 분석 완료

"""
    )



if __name__ == "__main__":

    main()
