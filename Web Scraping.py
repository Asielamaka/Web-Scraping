import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-1.html"

page = requests.get(url)
# # print(page.text)

# # To extract the part I need from the webpage
soup = BeautifulSoup(page.text, "html.parser")
# #print(soup.title.text)

# current_page = 1
# data = []
# proceed = True

# while (proceed == True):
#     print("Currently scraping page: " +str(current_page))
#     url = "https://books.toscrape.com/catalogue/page-" + str(current_page)+".html"
          
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, "html.parser")

#     if soup.title.text == "404 Not Found":
#         proceed = False

#     else:
all_books = soup.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
for books in all_books:
    item = {}
    item ['Title'] = books.find("img").attrs['alt']
    # item ['Link'] = "https://books.toscrape.com/catalogue/" + books.find("a").attrs['href']
    # item ['Price'] = books.find("p", class_="price_color").text[2:]
    # item ['Stock'] = books.find("p", class_="instock availability").text.strip()
    
    # data.append(item)
    print (item ['Title'])

    # current_page += 1
    #proceed = False
            
# df = pd.DataFrame(data)
# df.to_excel("books.xlsx")
# df.to_csv("books.csv")






