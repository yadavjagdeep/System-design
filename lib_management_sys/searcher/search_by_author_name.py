from book_searcher import BaseBookSearcher

class SearchByAuthorName(BaseBookSearcher):

    def __init__(self, author_name: list):
        self.author_name = author_name

    def search(self) -> list:
        pass
