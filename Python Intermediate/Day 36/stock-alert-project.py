import requests
import schedule
from datetime import time

# ------------------------ GET API CALL AND DATA -------------------------------
AV_Endpoint = "https://www.alphavantage.co/query"
parameters = {"function": "TIME_SERIES_DAILY",
              "symbol": "TSLA",
              "apikey": "02BNS6UMGNHD9WQI"
              }
response = requests.get(AV_Endpoint, params=parameters)
print(response.raise_for_status())
data = response.json()
# print(data)

# ------------------------ GET CLOSING PRICES -------------------------------
# Converting Dict into list to get index then fetching it
list_data = []
dict_data = data['Time Series (Daily)']

for i in dict_data:
    list_data.append(i)

yest_date = list_data[0]
prev_date = list_data[1]

yesterday_closing = data['Time Series (Daily)'][yest_date]['4. close']
previous_day_closing = data['Time Series (Daily)'][prev_date]['4. close']
print(yesterday_closing)
print(previous_day_closing)


#------------------------  CALCULATE % Change ------------------------
def calculate_percentage_change(previous_close, latest_close):
    price_difference = latest_close - previous_close
    percentage_change = (price_difference / previous_close) * 100
    return percentage_change


stock_change = calculate_percentage_change(float(previous_day_closing), float(yesterday_closing))
print(round(stock_change, 2), "%")


# ----------------------- DETECT If CHANGE IN PRICE ----------------
def is_significant_change(stock_price):
    return abs(stock_price) >= 2


# ------------------- FETCH NEWS DATA ---------------------
def fetch_news_data():
    NEWS_Endpoint = "https://newsapi.org/v2/everything"  # ?q=tesla&sortBy=publishedAt&apiKey=2be717943a7f452b835b8a8204f4d40b
    NEWS_API_KEY = "2be717943a7f452b835b8a8204f4d40b"
    news_parameters = {"q": "tesla",
                       "language": "en",
                       "sortBy": "publishedAt",
                       "apiKey": NEWS_API_KEY}
    news_response = requests.get(NEWS_Endpoint, params=news_parameters)
    news_response.raise_for_status()
    news_articles = news_response.json()
    return news_articles


# # ------------------------------ GET NEWS ------------------------------
def extract_news_articles():
    news_data = fetch_news_data()
    stock_news = []
    for i in range(3):
        title = news_data["articles"][i]["title"]
        description = news_data["articles"][i]["description"]
        published_date = news_data["articles"][i]["publishedAt"]
        article = {"title": title, "description": description,"publishedAt":published_date}
        stock_news.append(article)
    return stock_news


# -------------------- SEND TELEGRAM MESSAGE --------------------
# - get token say start get then id from - https://api.telegram.org/botTOKENgetUpdates

def monitor_stock():

    def send_telegram_message(message):
        BOT_TOKEN = "8834938535:AAHRXKiLecPlxScReSr1BqPHSfEzcGG2fgg"
        CHAT_ID = "1439202338"
        telegram_endpoint = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        telegram_parameters = {
            "chat_id": CHAT_ID,
            "text": message
        }
        telegram_response = requests.get(
            telegram_endpoint,
            params=telegram_parameters
        )
        telegram_response.raise_for_status()


    # --------------------- IF there is BIG movement extract news and send msg ------------
    if is_significant_change(stock_price=stock_change):

        news_data = extract_news_articles()

        for news in news_data:
            title = news["title"]
            description = news["description"]
            published_date = news["publishedAt"]
            message = (f"📈 TSLA Stock Alert\n \nStock moved by {round(stock_change, 2)}%\n"
                       f"\n📰 Headline:{title}\n"
                       f"\n📄 Summary:{description}\n"
                       f"\n📅 Date: {published_date}")


            send_telegram_message(message)


# -------------------- SCHEDULER --------------------

schedule.every().day.at("09:00").do(monitor_stock)
print("Stock Alert Bot Running...")

while True:
    schedule.run_pending()
    time.sleep(1)

