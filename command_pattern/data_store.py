
class TagStore:
    _TAGS = ["knapsack", "math", "mathematics", "sieve", "runtime error"]

    @classmethod
    def get_tags(cls):
        return cls._TAGS

    @classmethod
    def delete(cls, name: str):
        cls._TAGS.remove(name)

    @classmethod
    def insert(cls, name: str):
        cls._TAGS.append(name)
