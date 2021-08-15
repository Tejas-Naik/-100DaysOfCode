import requests
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_API_KEY = 'C8G6MM0KMJ7DCRMK'    # alfavantage.co for stock prices
NEWS_API_KEY = 'ab0ee07a9d694229ba7fab4a99cfac18'    # https://newsapi.org/

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameter = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
response = requests.get('https://www.alphavantage.co/query', params=parameter)
response.raise_for_status()
data = response.json()
dates = response.json()['Time Series (Daily)']

last_days_price = []

for day in dates:
    if len(last_days_price) < 2:
        last_days_price.append(dates[day]['4. close'])

today_starting_price = float(last_days_price[0])
yesterday_starting_price = float(last_days_price[1])

percentage = (100 * (yesterday_starting_price - today_starting_price)) / yesterday_starting_price
percentage = round(percentage, 2)
print(percentage)

if percentage >= 5 or percentage <= -5:

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # Init
    newsapi = NewsApiClient(api_key='ab0ee07a9d694229ba7fab4a99cfac18')
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                              # sources='bbc-news,the-verge',
                                              category='business',
                                              language='en',
                                              country='us')
    message_header = top_headlines['articles'][0]['title']
    message_desc = top_headlines['articles'][0]['description']




    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = 'ACd4d24d4a7c4d517dc8bb3a9d11782be2'
    auth_token = 'e14f948ddf1f39ddf812d758fda38790'
    client = Client(account_sid, auth_token)
    # messagge
    if percentage > 0:
        message_symb = '🔺'
    elif percentage < 0:
        message_symb = '🔻'
    message = client.messages \
                    .create(
                         body=f"TSLA: {message_symb} {percentage}%\n{message_header}\n{message_desc}",
                         from_='+12133720118',
                         to='+918151039620'
                     )
    print(message.sid)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

