from calculate_fuel import get_required_fuel


def test_mission_apollo_11():
    equipment_weight = 28801
    arguments = [(9.807, 1.62), (1.62, 9.807)]
    weight_fuel = 51898
    assert get_required_fuel(equipment_weight, arguments) == weight_fuel


def test_mars_mission():
    equipment_weight = 14606
    arguments = [(9.807, 3.711), (3.711, 9.807)]
    weight_fuel = 33388
    assert get_required_fuel(equipment_weight, arguments) == weight_fuel


def test_passenger_ship():
    equipment_weight = 75432
    arguments = [(9.807, 1.62), (1.62, 3.711), (3.711, 9.807)]
    weight_fuel = 212161
    assert get_required_fuel(equipment_weight, arguments) == weight_fuel