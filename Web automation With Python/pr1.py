import html5lib
import requests
from  bs4 import BeautifulSoup


res = requests.get("https:/www.consumerreports.org")

soup = BeautifulSoup(res.content, 'html5lib')

div_shop_deals = soup.find('div', attrs={"id": "shop-deals"})
print(div_shop_deals)