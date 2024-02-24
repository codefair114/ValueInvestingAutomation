import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_public_company_list():
    url = "https://www.sec.gov/files/company_tickers.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame.from_dict(data, orient="index")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def main():
    public_companies = get_public_company_list()

    print(public_companies)
if __name__ == "__main__":
    main()
