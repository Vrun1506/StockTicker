import requests
from bs4 import BeautifulSoup
import yfinance as yf

# Prompt the user for the stock symbol
stock_symbol = input("Enter the stock symbol: ").upper()

# URL for the stock on Yahoo Finance
url = f'https://uk.finance.yahoo.com/quote/{stock_symbol}/'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the current stock price based on the HTML structure
price_tag = soup.find('fin-streamer', {'data-symbol': stock_symbol, 'data-field': 'regularMarketPrice'})

# Check if the price was scraped successfully
if price_tag:
    scraped_price = float(price_tag.text.replace(",", ""))
    print(f"Scraped {stock_symbol} Stock Price:", scraped_price)
else:
    print(f"Could not find the stock price for {stock_symbol} on Yahoo Finance.")
    scraped_price = None

# Fetch the stock price using yfinance for comparison
stock = yf.Ticker(stock_symbol)
live_data = stock.history(period="1d")
yfinance_price = live_data['Close'].iloc[-1] if not live_data.empty else None

if yfinance_price:
    print(f"yfinance {stock_symbol} Stock Price:", yfinance_price)
else:
    print(f"Could not retrieve the stock price for {stock_symbol} using yfinance.")

# Compare the scraped price with yfinance price
if scraped_price and yfinance_price:
    if abs(scraped_price - yfinance_price) < 0.1:
        print("The prices match closely.")
    else:
        print("The prices do not match. There may be a discrepancy.")
else:
    print("Comparison not possible due to missing data.")
