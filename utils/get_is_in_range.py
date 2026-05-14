def get_is_in_range(base_coordinates, base_range, target_coordinates):
    for i in range (2):
        distance = abs(base_coordinates[i] - target_coordinates[i])
        print(f'Comparing {base_coordinates[i]} to {target_coordinates[i]}')
        print(f'Distance is {distance} and range is {base_range}')

        if abs(base_coordinates[i] - target_coordinates[i]) > base_range:
            return False

    return True
