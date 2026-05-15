from utils.get_is_in_range import get_is_in_range

class Unit:
    def __init__(self, name, hp, movement, position, can_attack, can_self_defend, attack_range, attack_damage, owner):
        self.name = name
        self.hp = hp
        self.movement = movement
        self.position = position
        self.can_attack = can_attack
        self.can_self_defend = can_self_defend
        self.attack_range = attack_range
        self.attack_damage = attack_damage
        self.owner = owner
    
    def __del__(self):
        print(f"Unit {self.name} has been killed!")

    def attack(self, enemy):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        
    def move_to(self, coordinates):
        pass