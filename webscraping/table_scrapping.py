import requests
import bs4
import csv

result_source_code = requests.get('https://pincode.app/andhra-pradesh/ananthapur')

soup = bs4.BeautifulSoup(result_source_code.text, 'html.parser')
# Extract table headers
headers = [th.text.strip() for th in soup.find("thead").find_all("th")]
# Print extracted data
print("Headers:", headers)

# Extract table rows
rows = []
for tr in soup.find("tbody").find_all("tr"):
    row = [td.text.strip() for td in tr.find_all("td")]
    rows.append(row)

    
# with open('table_data.txt', 'w+',  encoding='utf-8') as f:
#     f.write('\t'.join(headers) + '\n')  # Write headers
#     for row in rows:
#         f.write('\t'.join(row) + '\n')  # Write rows

# Write to CSV file
with open('table_data.csv', 'w+', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(headers)  # Write headers
    writer.writerows(rows)  # Write rows
