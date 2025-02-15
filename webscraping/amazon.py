import requests
import bs4

res = requests.get('https://amazon.com')
soup = bs4.BeautifulSoup(res.text, "lxml")
print(soup)