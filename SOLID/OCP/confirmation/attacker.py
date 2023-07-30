class Attacker:

    def attack(self, super_hero: list):
        for sp_hero in super_hero:
            sp_hero.attack()



if __name__ == "__main__":
    from bat_man import BatMan
    from super_man import SuperMan
    from captain_america import CaptainAmerica
    _super_hero = [BatMan(), SuperMan(), CaptainAmerica(), SuperMan()]
    Attacker().attack(_super_hero)
