class DBAccessor:

    def getBookWithNames(self, book_name: str):
        pass

    def getBookWithAuthorName(self, author_names: list):
        pass

    def getMemberWithName(self, member_name: str):
        pass


    def insertBookCopy(self, book_copy: object):
        pass

    def deleteBookCopy(self, book_copy: object):
        pass

    def markAsBlocked(self, member: object):
        pass

    def issueBookCopyToMember(self, book_copy: object, member: object):
        pass

    def submitBookCopyFromMember(self, book_copy: object, member: object):
        pass

    def isCopyAvailable(self):
        pass

