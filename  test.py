# import yfinance as yf
# import pandas as pd
# import requests
# from tldr_python import TLDR



# stock = "microsoft"
# ticker = yf.Ticker("msft")
# tldr = TLDR("ca311ddc08msh3530fb8fa9aa773p178701jsne53b8b9a2d65")

# df = pd.read_csv("Stockdata/stocks-list.csv")

# link =  ticker.news[0]['link']
# title = ticker.news[0]['title']
# summary = tldr.summarize(ticker.news[0]['link'], max_sentences=2).text


# print(df['Company Name'].tolist())



# import csv

# with open('../Stockdata/stocks-list.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # Skip the header row if present

#     stocks = [Stock(name=row[1], ticker=row[0]) for row in reader]

# Stock.objects.bulk_create(stocks)