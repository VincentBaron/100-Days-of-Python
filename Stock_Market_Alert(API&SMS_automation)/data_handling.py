import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "6GGC35ZZGRXGHG7S"
NEWS_API_KEY = "669df9859b1748dbbc076b67d428f040"
ACCOUNT_SID = "ACb30b41a896db509636494254ad27bd14"
AUTH_TOKEN = "2fcf9669aa608ec091e6602aabe2847e"


def get_news():
    news_params = {
        "q": "tesla",
        "apikey": NEWS_API_KEY
    }
    news_api = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_api.raise_for_status()
    news_data = news_api.json()["articles"][:3]
    return news_data


def get_stocks():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": API_KEY
    }

    api = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
    api.raise_for_status()
    data = api.json()
    yest_closing = float(data["Time Series (Daily)"]["2021-02-03"]["4. close"])
    bef_yest_closing = float(data["Time Series (Daily)"]["2021-02-02"]["4. close"])

    pos_dif = abs(yest_closing - bef_yest_closing)
    pos_dif_per = pos_dif * 100 / bef_yest_closing
    return pos_dif_per


def send_text(news):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for i in range(0, 3, 1):
        headline = news[i]["title"]
        content = news[i]["description"]
        message = client.messages \
            .create(
            body=f"\n\nHeadline: {headline}\n\nBrief:{content}",
            from_='+15613366563',
            to='+33695143200'
        )
        print(message.status)
