"""
To implement tag manager, we will be using a universally accepted design patter call as 'Command Pattern'.

The idea is to abstract out all the operations, and the tag manager will only depend on that abstract class to
perform the operation.

Saying more concrete, insert, delete, update etc. is nothing but commands only that are needs to be executed

"""

from command_pattern.confirmation.commands import Command


class TagManager:

    def __init__(self, command: Command):
        self.command = command

    def change_tag(self):
        self.command.execute()

