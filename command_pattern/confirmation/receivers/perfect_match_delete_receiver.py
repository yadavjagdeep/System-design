from command_pattern.confirmation.receivers import *


class PerfectMatchDeleter:

    @classmethod
    def delete(cls, tag: str):
        tags: list = TagStore.get_tags()

        TagStore.delete(tag) if tag in tags else print(f"Unknown tag = {tag}")
