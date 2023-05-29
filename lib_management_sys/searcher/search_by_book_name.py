from book_searcher import BaseBookSearcher

class SearchByBookName(BaseBookSearcher):

    def __init__(self, book_name: str):
        self.book_name = book_name

    def search(self):
        pass

