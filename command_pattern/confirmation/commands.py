"""
One Important thing to take a note here is that we should not have much business logic in command itself rather they
should have a receiver that they will deligate the command to execute the logic.
"""

from command_pattern import *
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        raise NotImplemented("Subclass must implement the execute method")


class InsertCommand(Command):

    def execute(self):
        pass


class DeleteCommand(Command):

    def __init__(self, name: str, perfect_match_deleter: PerfectMatchDeleter):
        self.name = name
        self.perfect_match_deleter = perfect_match_deleter

    def execute(self):
        self.perfect_match_deleter.delete(self.name)


class DeleteByRegexCommand(Command):

    def __init__(self, pattern: str, partial_match_deleter: PartialMatchDeleter):
        self.pattern = pattern
        self.partial_match_deleter = partial_match_deleter

    def execute(self):
        self.partial_match_deleter.delete(self.pattern)


class UpdateTagmanagerCommand(Command):

    def execute(self):
        pass
