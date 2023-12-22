import requests

from pages.quotes_page import QuotePages

page_content = requests.get('https://quotes.toscrape.com/').content
page = QuotePages(page_content)

for quote in page.quotes:
    print(quote.author)
