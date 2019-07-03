# SCRAPING REVIEW DATA FROM CSV FILE
import requests
from bs4 import BeautifulSoup
import csv

#Read input url dari file csv & write output review
with open('best-novel-url.csv', newline='') as f_urls, open('data-review.csv', 'w', newline='', encoding="utf-8") as f_output:
    csv_urls = csv.reader(f_urls)
    csv_output = csv.writer(f_output)
    csv_output.writerow(['Nama', 'Ulasan', 'Rating'])
    
    # Collecting & parsing konten web
    for line in csv_urls:
        r = requests.get(line[0]).text
        soup = BeautifulSoup(r, 'lxml')
   
        # Find elemen class review di dalam id bookReviews
        novel_review_list = soup.find('div', {'id': 'bookReviews'})
        novel_review_list_items = novel_review_list.find_all(class_='review')
        
        # Get masing-masing nama & review dari class bookReviews
        for novel_review in novel_review_list_items:
            name = novel_review.find(class_='user').get_text()
            review = novel_review.find(class_='readable').find('span', recursive=False).get_text()
            rating_element = novel_review.find('span', {'size': '15x15'})
            # Skip item review ketika elemen rating tidak ditemukan
            if rating_element == None:                
                continue
            else :
                rating = rating_element.get_text()

            csv_output.writerow([name, review, rating])
