# SCRAPING URL ADDRESS
import requests
import csv
from bs4 import BeautifulSoup

# Write ke file csv
csv_output = csv.writer(open('best-novel-url.csv', 'w', newline=''))

pages = []

# Collecting & parsing konten Web hlm 1-6
for i in range(1, 7):
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
        link = 'https://www.goodreads.com' + novel_title.get('href') + '?language_code=id'

        csv_output.writerow([link])
