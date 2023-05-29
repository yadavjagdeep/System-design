"""
=> By visualising GUI, we can think of what all apis we need in the app

$ Home page view
1. searchByBookName(book_name: str)
2. searchByAuthorName(author_name: str)
3. searchByMemberName(member_name: str)
4. searchByMemberId(member_id: str)

$ Admin view
1. addBook(book_data: dict, token: str)
2. deleteBook(book_id: str, token: str)
3. issueBook(book_id: str, member_id: str, token: str)
4. submitBook(book_id: str, member_id: str, token: str)
5. blockMember(member_id: str, token)

$ common view
1. borrowedBook(member_id: str)
"""