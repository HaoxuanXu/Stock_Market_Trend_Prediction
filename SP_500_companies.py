# from libraries
import requests
from bs4 import BeautifulSoup

# from files
import auth

url = "https://www.slickcharts.com/sp500"


def get_sp_500(url, headers):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        raw_list = [a['href'] for a in soup.find_all('a')]
        ticker_list = list(set([a.replace('/symbol/', '') for a in raw_list if ('symbol' in a)]))
        return ticker_list
        print("Process Complete!")
    else:
        print("Connection Failed... Error Code:{}".format(str(page.status_code)))


# ticker_list = get_sp_500(url=url, headers=headers)
