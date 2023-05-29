from auth.user_authanticator import UserAuthenticator

class Tester:

    def searchByBookName(self, book_name: str):
        if not book_name:
            raise AttributeError("Book name cannot be Null !!!")

        from searcher.search_by_book_name import SearchByBookName
        BookSearcher = SearchByBookName(book_name)
        return BookSearcher.search()

    def searchByAuthorName(self, author_name: list):
        if not author_name or len(author_name) == 0:
            raise AttributeError("Author name cannot be Null !!!")

        from searcher.search_by_author_name import SearchByAuthorName
        BookSearcher = SearchByAuthorName(author_name)
        return BookSearcher.search()

    def searchByMemberName(self, member_name: str, token):
        if not member_name:
            raise AttributeError("Member name cannot be Null !!!")
        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")

        from searcher.search_by_member_name import SearchByMemberName
        BookSearcher = SearchByMemberName(member_name)
        return BookSearcher.search()

    def searchByMemberId(self, member_id: list, token):
        if not member_id:
            raise AttributeError("Member id cannot be Null !!!")

        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")

        from searcher.search_by_member_id import SearchByMemberId
        BookSearcher = SearchByMemberId(member_id)
        return BookSearcher.search()

    def addBook(self, book_name: str, publicationDate: str, author: str, token: str):
        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")

        """
        Validation logic goes here
        """
        from book.book_details import BookDetails
        from book.book_copy import BookCopy
        from id_genrator.book_copy_id_genrator import BookCopyIdGenerator
        book_copy: object = BookCopy(BookDetails(book_name=book_name, publication_date=publicationDate, author=author), book_id=BookCopyIdGenerator.getUniqueBookCopyId(book_name))

        from library.library import Library
        Library().addBook(book_copy)


    def deleteBook(self, book_copy_id: list, token: str):
        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")

        if not book_copy_id:
            raise AttributeError("Book copy Id cannot be null !!!")

        from searcher.search_book_by_id import SearchBookById
        book_copies = SearchBookById(book_copy_id).search()
        if not book_copies:
            raise RuntimeError("No book copies found for the copy_ids")

        from library.library import Library
        for item in book_copies:
            Library().deleteBook(item)


    def issueBook(self, book_copy_ids: list, member_id: str, token: str):
        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")

        if not book_copy_ids or not member_id:
            raise AttributeError("Book copy ids or member ids cannot be null !!!")

        from searcher.search_book_by_id import SearchBookById
        book_copies = SearchBookById(book_copy_ids).search()
        if not book_copies:
            raise RuntimeError("No book copy found with the given ids")

        from searcher.search_by_member_id import SearchByMemberId
        member = SearchByMemberId([member_id]).search()
        if not member:
            raise RuntimeError("No member found with given member id")

        from library.library import Library
        for book_copy in book_copies:
            Library().issueBook(book_copy, member)

    def submitBook(self, book_copy_ids: list, member_id: str, token: str):
        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")
        if not book_copy_ids or not member_id:
            raise AttributeError("Book copy ids or member ids cannot be null !!!")

        from searcher.search_book_by_id import SearchBookById
        book_copies = SearchBookById(book_copy_ids).search()
        if not book_copies:
            raise RuntimeError("No book copy found with the given ids")

        from searcher.search_by_member_id import SearchByMemberId
        member = SearchByMemberId([member_id]).search()
        if not member:
            raise RuntimeError("No member found with given member id")

        from library.library import Library
        for book_copy in book_copies:
            Library().submitBook(book_copy, member)


    def blockMember(self, member_id: str, token):
        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")

        if not member_id:
            raise AttributeError("Member id cannot be None !!!")

        from searcher.search_by_member_id import SearchByMemberId
        members = SearchByMemberId([member_id]).search()
        if not members:
            raise RuntimeError("No member found with the provided member id !!!")

        from library.library import Library
        for member in members:
            Library().blockMember(member)


    def borrowedBook(self, member_id: str) -> list[object]:
        if not member_id:
            raise AttributeError("Member id cannot be null !!!")

        from searcher.search_by_member_id import SearchByMemberId
        member = SearchByMemberId([member_id]).search()
        if not member:
            raise RuntimeError("No member with the provided member id")

        from library.library import Library
        Library().getBorrowedBooks(member)

    def getBorrowerOfBooks(self, book_copy_id: str, token: str) -> object:
        if not UserAuthenticator.isAdmin(token):
            raise PermissionError("User is not authorised to perform the operation")

        if not book_copy_id:
            raise AttributeError("Book copy id cannot be null !!!")

        from searcher.search_book_by_id import SearchBookById
        book_copy = SearchBookById([book_copy_id]).search()
        if not book_copy:
            raise RuntimeError("No book copy with the provided book copy id")

        from library.library import Library
        member = Library().getBorrower(book_copy)
        if not member:
            raise RuntimeError("No Borrower of the provided book copy id")

        return member