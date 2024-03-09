from command_pattern.confirmation.receivers import *


class TagInserter:

    @classmethod
    def insert_tag(cls, name: str):
        TagStore.insert(name)
