import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = "https://books.toscrape.com/catalogue/page-1.html"
# book = requests.get(url)
# print (book.text)

# soup = BeautifulSoup(book.text, "html.parser")
# print(soup.title.text)

page = 1
scraped_data = []
while page <= 50:

    url = "https://books.toscrape.com/catalogue/page-" + str(page) + ".html"
    book = requests.get(url)
    soup = BeautifulSoup(book.text, "html.parser")

    books = soup.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
    
    for each_book in books:
        Item_to_find = {}
        Item_to_find['Title'] = each_book.find("h3").find("a").attrs['title']
        Item_to_find['Link'] = "https://books.toscrape.com/catalogue/" + each_book.find("a").attrs['href']
        Item_to_find['Availability'] = each_book.find("p", class_ = "instock availability").text.strip()
        Item_to_find['Price'] = each_book.find("p", class_ = "price_color").text.strip().replace("Â", "")
       
        # print (cleaned_price)
        scraped_data.append(Item_to_find)
    page += 1

df = pd.DataFrame(scraped_data)
df.to_excel("Scraped Book Info.xlsx", index = False) 
