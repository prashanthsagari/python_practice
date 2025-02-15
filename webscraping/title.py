import requests
import bs4

result = requests.get("http://google.com")
# print(result.text)
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('a')[0].get_attribute_list('href')[0])

