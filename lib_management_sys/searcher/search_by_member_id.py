from member_searcher import BaseMemberSearcher

class SearchByMemberId(BaseMemberSearcher):

    def __init__(self, member_ids: list):
        self.member_id = member_ids

    def search(self) -> list:
        pass

