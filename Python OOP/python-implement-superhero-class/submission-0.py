class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
        pass


# TODO: Create Superhero instances
my_hero1 = SuperHero('Batman','Intelligence',100)
my_hero2 = SuperHero('Superman','Strength',150)

# TODO: Print out the attributes of each superhero
print(my_hero1.name)
print(my_hero1.power)
print(my_hero1.health)
print(my_hero2.name)
print(my_hero2.power)
print(my_hero2.health)
