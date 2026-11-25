import yfinance as yf
import pandas as pd


def get_price_data(ticker, period="1y"):

    data = yf.download(
        ticker,
        period=period,
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data


def get_qqq():

    return get_price_data("QQQ")


def get_vix():

    return get_price_data("^VIX")


def get_dxy():

    return get_price_data("DX-Y.NYB")


def get_us10y():

    return get_price_data("^TNX")
