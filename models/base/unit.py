from utils.get_is_in_range import get_is_in_range

class Unit:
    def __init__(self, name, hp, movement, position, can_attack, attack_range, attack_damage, owner):
        self.name = name
        self.hp = hp
        self.movement = movement
        self.position = position
        self.can_attack = can_attack
        self.attack_range = attack_range
        self.attack_damage = attack_damage
        self.owner = owner

    def attack(self, enemy):
        if self.owner == enemy.owner:
            raise Exception('Cannot attack friendly units')

        if not get_is_in_range(self.position, self.attack_range, enemy.position):
            raise Exception('{} is out of range').format(enemy.name)

