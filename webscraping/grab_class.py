import requests
import bs4

# res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# soup = bs4.BeautifulSoup(res.text, "lxml")
# print(soup.select('.vector-dropdown-content')[0].getText())

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text,'lxml')
# print(len(soup.select('.mw-file-description')))
comp = soup.select('.mw-file-element')[0]
# print(comp['src'])
# print(comp.attrs)

for image in soup.select('.mw-file-element'):
    print(image['src'])
