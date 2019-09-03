import requests
from bs4 import BeautifulSoup

url = "https://www.slickcharts.com/sp500"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def get_sp_500(url, headers):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        print("Connection Established!")

    soup = BeautifulSoup(page.content, "html.parser")
    raw_list = [a['href'] for a in soup.find_all('a')]
    ticker_list = list(set([a.replace('/symbol/', '') for a in raw_list if ('symbol' in a)]))
    return ticker_list
    print("Process Complete!")


ticker_list = get_sp_500(url=url, headers=headers)
