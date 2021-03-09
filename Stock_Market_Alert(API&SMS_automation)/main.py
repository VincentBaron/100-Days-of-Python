from data_handling import *

percent_dif = get_stocks()
if percent_dif < 5:
    news = get_news()
    send_text(news)


