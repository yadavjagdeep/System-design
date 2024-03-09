"""
To improve on a solution written in Violation1 the first thing comes to our mind is to make tag manager abstract and
have concrete implementation for each operation

The below solution might look like a correct solution it's also not violating the solid principles, but it does have
design flows.

Let me put it in this way
While writing a class we are supposed to abstract out the operations that are supposed to be modified and
updated over-time.

Now we have abstracted out Tag manager the whole class it is supposed to have get tag manager, which will not change
then no point to have concrete implementation of TagManager class to support list_tags
"""

from abc import ABC, abstractmethod


class TagManager(ABC):

    @abstractmethod
    def manage(self):
        raise NotImplemented


class InsertTagManager(TagManager):

    def manage(self):
        pass


class DeleteTagManager(TagManager):

    def manage(self):
        pass


class DeleteByRegexTagManager(TagManager):

    def manage(self):
        pass


class UpdateTagManager(TagManager):

    def manage(self):
        pass


class ListTagManager(TagManager):

    def manage(self):
        pass
