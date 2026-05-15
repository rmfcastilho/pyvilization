class City:
    def __init__(self, name, resources, population, hp, is_capital, owner):
        self.name = name
        self.resources = resources
        self.population = population
        self.hp = hp
        self.is_capital = is_capital

    def turn_into_capital():
        self.is_capital = True

    def change_ownership(previous_owner, new_owner):
        new_owner.obtain_city(self)
        previous_owner.