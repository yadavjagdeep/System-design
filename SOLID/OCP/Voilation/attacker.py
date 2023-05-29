from OCP_Open_Closed_Principe import SuperHero


class Attacker:

    def attack_with_super_hero(self, superHero: list):
        for super_hero in superHero:
            if super_hero == SuperHero.BAT_MAN:
                SuperHero.BAT_MAN.attack_with_bat_man()
            elif super_hero == SuperHero.SUPER_MAN:
                SuperHero.SUPER_MAN.attack_with_super_man()
            elif super_hero == SuperHero.CAPTAIN_AMERICA:
                SuperHero.CAPTAIN_AMERICA.attack_with_captain_america()
            else:
                raise Exception(f"Unknown Super Hero {super_hero}")


if __name__ == "__main__":
    _super_hero = [SuperHero.BAT_MAN, SuperHero.SUPER_MAN, SuperHero.CAPTAIN_AMERICA]
    Attacker().attack_with_super_hero(_super_hero)
