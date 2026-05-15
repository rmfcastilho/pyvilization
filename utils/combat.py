from get_is_in_range import get_is_in_range


def unit_to_unit_combat(attacker, defender):
    if attacker.owner == defender.owner:
        raise Exception('Cannot attack friendly units')

    if not attacker.can_attack:
        raise Exception(f'${attacker.name} cannot attack other units')

    if not get_is_in_range(attacker.position, attacker.attack_range, defender.position):
        raise Exception(f'{defender.name} is out of range')
    
    if defender.can_self_defend:
        print(f'{defender.name} preemptively attacks {attacker.name} for {defender.attack_damage} damage')
        attacker.hp -= defender.attack_damage

        if attacker.hp <= 0:
            del attacker
            return

    print(f'{attacker.name} attacks {defender.name} for {attacker.attack_damage} damage')

    defender.hp -= attacker.attack_damage

    if attacker.hp <= 0:
        attacker.move_to(defender.position)
        del defender
        
        return


def unit_to_city_combat(city, unit):
    pass