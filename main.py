import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_eod_data(ticker):
    url = f"http://api.marketstack.com/v2/eod?access_key={API_KEY}&symbols={ticker}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["data"][0]

def main():
    print("Welcome to the Stock Market Data App.")
    ticker = input("Enter a stock ticker: ").upper()
    print()
    
    try:
        print(f"Showing stock data for {ticker}...")
        stock_data = get_eod_data(ticker)
        print(f"High: {stock_data["high"]}")
        print(f"Low: {stock_data["low"]}")
        print(f"Close: {stock_data["close"]}")
    except:
        print(f"Could not find {ticker}. Please try again.")

if __name__ == "__main__":
    main()