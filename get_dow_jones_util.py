# from libraries
import requests
from bs4 import BeautifulSoup

# from files
import auth

url = "https://money.cnn.com/data/dow30/"

def get_dow_jones(url, headers):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        raw_list = [a['href'] for a in soup.find_all('a', attrs={"class": "wsod_symbol"})]
        tickers = [a.split("=")[1] for a in raw_list]
        print("Process Complete!!!")
        return tickers
    else:
        print("Connection Failed... Error Code:{}".format(str(page.status_code)))