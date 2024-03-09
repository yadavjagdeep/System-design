from command_pattern.confirmation.command_factory import CommandFactory
from command_pattern.confirmation.tag_manager import TagManager


class TagsApi:

    @classmethod
    def operation_tags(cls, command_name: str):
        command = CommandFactory.get_command(command_name)
        TagManager(command).change_tag()
        return {"Operation on command success"}, 200



