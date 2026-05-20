class Civilization:
    def __init__(self, name, modifiers, resources, wonders, cities):
        self.name = name
        self.modifier = modifiers
        self.resources = resources
        self.wonders = wonders
        self.cities = cities

    def found_city(self):
        self.cities.append(get_standard_city_name())
    
    def obtain_city(self, city):
        self.cities.append(city)
    
    def remove_city(self, city):
        self.cities.remove(city)

def get_standard_city_name():
    print("Don't forget to implement this")
    return 'IMPLEMENT THIS'