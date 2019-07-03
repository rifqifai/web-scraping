# SCRAPING URL DATA
import requests
import csv
from bs4 import BeautifulSoup

# Write ke file csv
f = csv.writer(open('best-novel.csv', 'w', newline=''))
f.writerow(['Title', 'Link'])

pages = []

# Collecting & parsing konten Web
for i in range(1, 5):
    url = 'https://www.goodreads.com/list/show/67567.Novel_Indonesia_Terbaik?page=' + str(i)
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Find elemen class bookTitle di dalam class tableList
    novel_title_list = soup.find(class_='tableList')
    novel_title_list_items = novel_title_list.find_all(class_='bookTitle')
    
    # Get masing-masing title dan url dari class tableList
    for novel_title in novel_title_list_items:
        title = novel_title.find('span',{'itemprop':'name'}).get_text()
        link = 'https://www.goodreads.com' + novel_title.get('href')

        f.writerow([title, link])
