from member_searcher import BaseMemberSearcher

class SearchByMemberName(BaseMemberSearcher):

    def __init__(self, member_name: str):
        self.member_name = member_name

    def search(self) -> list:
        pass