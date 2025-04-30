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
    apple_stock_data = get_eod_data("AAPL")
    
    print(apple_stock_data["open"])
    print(apple_stock_data["high"])
    print(apple_stock_data["low"])
    print(apple_stock_data["close"])

if __name__ == "__main__":
    main()