"""
 -Class should be open for extension but closed for modification
"""
# let's create a superHero class to understand this a bit more

from enum import Enum

class SuperHero(Enum):

    """
     -{**IMP**} Methods of an enum class are associated with enum attributes not with the class
    """

    BAT_MAN = "BAT_MAN"
    SUPER_MAN = "SUPER_MAN"
    CAPTAIN_AMERICA = "CAPTAIN_AMERICA"

    def attack_with_bat_man(self):
        print(f"{self.BAT_MAN.value} Attacking...")

    def attack_with_super_man(self):
        print(f"{self.SUPER_MAN.value} Attacking...")

    def attack_with_captain_america(self):
        print(f"{self.CAPTAIN_AMERICA.value} Attacking...")


# have invoked this in attacker file
"""
 -There are few problems with this approach
 
  1. If we need to add a new super hero say IRON_MAN we add it in SuperHero enum class with it's attack method,
   Now we also need to make changes in Attacker class to identify the superHero and invokes it attack method, else
   code will break.
   
  2. Attacker class needs to know about all the enum attributes to compare and invoke their respective attack method.
  
"""
" => This Violets OCP(Open Closed Principle), i.e Class/Module should we open for extension but closed for modification. "

" => One thing we can always do to insure that we are not violating OCP is we always code to abstraction and not ton concretion"
