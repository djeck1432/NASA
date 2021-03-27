

def get_fuel_launch(mass, gravity):
    additional_fuel = int(mass * gravity * 0.042 - 33)
    total_weight_fuel = additional_fuel
    while additional_fuel >= 0:
        additional_fuel = int(additional_fuel * gravity * 0.042 - 33)
        total_weight_fuel += additional_fuel if additional_fuel > 0 else 0
    return total_weight_fuel


def get_fuel_land(mass, gravity):
    additional_fuel = int(mass * gravity * 0.033 - 42)
    total_weight_fuel = additional_fuel
    while additional_fuel >= 0:
        additional_fuel = int(additional_fuel * gravity * 0.033 - 42)
        total_weight_fuel += additional_fuel if additional_fuel > 0 else 0
    return total_weight_fuel


def get_required_fuel(empty_rocket_mass, gravities):
    rocket_mass = empty_rocket_mass
    total_weight_fuel = 0
    for gravity in gravities[::-1]:
        gravity_launch, gravity_land = gravity
        land_fuel = get_fuel_land(rocket_mass, gravity_land)
        rocket_mass += land_fuel
        launch_fuel = get_fuel_launch(rocket_mass, gravity_launch)
        rocket_mass += launch_fuel
        total_weight_fuel += launch_fuel + land_fuel
    return total_weight_fuel


if __name__ == '__main__':
    get_required_fuel(empty_rocket_mass, gravities)