# SCRAPING REVIEW DATA FROM DIRECT URL
import requests
import csv
from bs4 import BeautifulSoup

# Write ke file csv
f = csv.writer(open('data-review.csv', 'w', newline=''))
f.writerow(['Nama', 'Ulasan'])

pages = []

url = 'https://www.goodreads.com/book/show/1362193.Laskar_Pelangi' + '?language_code=id'
pages.append(url)

# Collecting & parsing konten Web
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'lxml')
    
    # Find elemen class review di dalam id bookReviews
    novel_review_list = soup.find('div', {'id': 'bookReviews'})
    novel_review_list_items = novel_review_list.find_all(class_='review')

    # Get masing-masing name dan review dari id bookReviews
    for novel_review in novel_review_list_items:
        name = novel_review.find(class_='user').get_text()
        review = novel_review.find(class_='readable').find('span', recursive=False).get_text()

        f.writerow([name, review])
