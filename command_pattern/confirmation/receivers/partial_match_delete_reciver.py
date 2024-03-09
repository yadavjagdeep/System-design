from command_pattern.confirmation.receivers import *
import re


class PartialMatchDeleter:

    @classmethod
    def delete(cls, pattern: str):
        tags: list = TagStore.get_tags()
        for tag in tags:
            if re.match(pattern, tag):
                tags.remove(tag)
                return

        print(f"No Tag matched to pattern = {pattern}")
