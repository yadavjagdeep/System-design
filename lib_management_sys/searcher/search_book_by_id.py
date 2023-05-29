from book_searcher import BaseBookSearcher

class SearchBookById(BaseBookSearcher):

    def __init__(self, book_copy_id: list):
        self.book_copy_id = book_copy_id

    def search(self) -> list:
        pass