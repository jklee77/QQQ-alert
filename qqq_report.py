from data_loader import (
    get_qqq,
    get_vix,
    get_dxy,
    get_us10y
)


def main():

    print("==========================")
    print("QQQ AI 투자 리포트")
    print("==========================")


    qqq = get_qqq()
    vix = get_vix()
    dxy = get_dxy()
    us10y = get_us10y()


    qqq_price = float(
        qqq["Close"].iloc[-1]
    )

    vix_price = float(
        vix["Close"].iloc[-1]
    )

    dxy_price = float(
        dxy["Close"].iloc[-1]
    )

    rate = float(
        us10y["Close"].iloc[-1]
    )


    print(
        f"""
QQQ 현재가 :
${qqq_price:.2f}

VIX :
{vix_price:.2f}

달러지수 :
{dxy_price:.2f}

미국10년물 금리 :
{rate:.2f}

데이터 수집 완료
"""
    )


if __name__ == "__main__":
    main()
