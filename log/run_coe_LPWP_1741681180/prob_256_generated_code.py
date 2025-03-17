def minimize_transportation_units(trains, trams) -> int:
    """
    Args:
        trains: Number of trains (an integer).
        trams: Number of trams (an integer).

    Returns:
        total_transportation_units: Total number of transportation units (an integer).
    """
    train_capacity = 120
    tram_capacity = 30
    min_trains = 1
    min_trams = 2
    min_people = 600

    # Objective: minimize total number of transportation units
    total_transportation_units = trains + trams

    # Constraints
    if train_capacity * trains + tram_capacity * trams < min_people:
        raise ValueError("Capacity constraint not met. Minimum people requirement not satisfied.")
    if trams < 2 * trains:
        raise ValueError("Tram constraint not met. Number of trams must be at least twice the number of trains.")

    return total_transportation_units