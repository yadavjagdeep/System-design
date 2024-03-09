from command_pattern import *


class CommandFactory:
    __COMMANDS_MAP = {
        "perfectMatchDelete": PerfectMatchDeleter,
        "partialMatchDelete": PartialMatchDeleter,
        "insert": TagInserter,
        "update": TagUpdater
    }

    @classmethod
    def get_command(cls, command_name: str):
        command = cls.__COMMANDS_MAP.get(command_name)
        if not command:
            raise Exception(f"Unknown command = {command}, please match from = {cls.__COMMANDS_MAP.keys()}")

        return command()
