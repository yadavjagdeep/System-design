from factory_design_pattern.coffee_machine.coffee_server import CoffeeServer

if __name__ == "__main__":
    coffee_server = CoffeeServer("cappuccino")
    coffee_server.serve()

    latte_server = CoffeeServer("latte")
    latte_server.serve()

