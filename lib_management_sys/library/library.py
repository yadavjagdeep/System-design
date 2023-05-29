class Library:

    def __init__(self, db_accessor):
        self.db_accessor = db_accessor
    def addBook(self, book_copy: object):
        pass

    def deleteBook(self, book_copy: object):
        if not self.db_accessor().isCopyAvailable(book_copy):
            raise Exception("Book is not available in library !!!")
        self.db_accessor().deleteBookCopy(book_copy)

    def issueBook(self, book_copy: object, member: object):
        pass

    def submitBook(self, book_copy: object, member: object):
        pass

    def getBorrower(self, book_copy: object):
        pass

    def getBorrowedBooks(self, member: object):
        pass

    def blockMember(self, member: object):
        pass