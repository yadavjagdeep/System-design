from factory_design_pattern.coffee_machine.factories.coffee_factory import CoffeeFactory


class CoffeeServer:

    def __init__(self, coffee_type: str):
        self.coffee: object = CoffeeFactory.get_coffee(coffee_name=coffee_type)

    def serve(self):
        self.coffee.brew()
        self.coffee.boil()
        return self.coffee
