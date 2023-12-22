from bs4 import BeautifulSoup
from locator.quotes_page_locator import QuotePageLocator
from parser.quotes import QuoteParser


class QuotePages:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotePageLocator.QUOTE
        quotes_tag = self.soup.select(locator)
        return [QuoteParser(e) for e in quotes_tag]
