# import requests from bs4 import
#
#
# url = 'https://ca.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-tre-srch'
# page = requests.get(url)
# soup = BeautifulSoup4(page.text, 'lxml')
# price = soup.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
# print(price)