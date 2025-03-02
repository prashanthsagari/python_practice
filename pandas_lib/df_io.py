#  sqlalchemy lxml html5lib BeautifulSoup4
# pip install sqlalchemy
# pip install lxml
# pip install html5lib
# pip install BeautifulSoup4

import pandas as pd

df = pd.read_csv('example')

df.to_csv('custom_output')
df.to_csv('main', index=False)

print(pd.read_excel('Excel_Sample.xlsx'))

data = pd.read_html("https://fdic.gov/bank-failures/failed-bank-list")
print(data)
