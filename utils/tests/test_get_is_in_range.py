from ..get_is_in_range import get_is_in_range

def test_is_within_range():
    self_coordinates = [0, 5]
    self_attack_range = 3
    enemy_coordinates = [2, 4]

    assert get_is_in_range(self_coordinates, self_attack_range, enemy_coordinates)

def test_is_out_of_range():
    self_coordinates = [0, 5]
    self_attack_range = 1
    enemy_coordinates = [2, 4]

    assert get_is_in_range(self_coordinates, self_attack_range, enemy_coordinates) == False
