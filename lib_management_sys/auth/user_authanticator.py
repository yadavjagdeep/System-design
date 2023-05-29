class UserAuthenticator:

    @staticmethod
    def isAdmin(token: str)-> bool:
        return True

    @staticmethod
    def isMember(token: str) -> bool:
        return True