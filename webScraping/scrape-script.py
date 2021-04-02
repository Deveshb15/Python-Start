import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/quotes/tag/life"

def get_quotes(url):
    
    res = requests.get(url)

    soup = BeautifulSoup(res.text)

    quote_divs = soup.find_all("div", attrs={"class" : "quote"})

    quotes = []
    
    for quote_div in quote_divs:

        quote_Text = quote_div.find_next("div", attrs={"class" : "quoteText"}) 

        striped = quote_Text.text.strip()

        striped_li = striped.split("\n")

        quote = striped_li[0][1:-1]

        author = striped_li[-1].strip()

        quote_item = {
            "text" : quote,
            "author" : author
        }
        quotes.append(quote_item)

    return quotes

result = get_quotes(url)

str = ''.join(str(e) for e in result)

with open("quotes.txt", "w") as file:
    file.write(str)