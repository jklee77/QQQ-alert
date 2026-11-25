import matplotlib.pyplot as plt



def create_qqq_chart(df):


    plt.figure(figsize=(10,5))


    plt.plot(
        df.index,
        df["Close"],
        label="QQQ"
    )


    if "MA20" in df.columns:

        plt.plot(
            df.index,
            df["MA20"],
            label="20일 이동평균"
        )


    if "MA60" in df.columns:

        plt.plot(
            df.index,
            df["MA60"],
            label="60일 이동평균"
        )


    plt.title(
        "QQQ Technical Analysis"
    )


    plt.xlabel(
        "Date"
    )


    plt.ylabel(
        "Price"
    )


    plt.legend()


    file="qqq_chart.png"


    plt.savefig(
        file,
        bbox_inches="tight"
    )


    plt.close()


    return file
