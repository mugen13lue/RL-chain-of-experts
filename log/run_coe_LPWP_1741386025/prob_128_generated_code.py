def prob_128(liquid_hand_sanitizer, foam_hand_sanitizer, water, alcohol, available_water, available_alcohol, liquid_constraint, foam_constraint):
    """
    Args:
        liquid_hand_sanitizer: an integer, the number of liquid hand sanitizers made
        foam_hand_sanitizer: an integer, the number of foam hand sanitizers made
        water: an integer, the amount of water required for each hand sanitizer
        alcohol: an integer, the amount of alcohol required for each hand sanitizer
        available_water: an integer, the available amount of water
        available_alcohol: an integer, the available amount of alcohol
        liquid_constraint: an integer, the maximum number of liquid hand sanitizers that can be made
        foam_constraint: an integer, the maximum number of foam hand sanitizers that can be made

    Returns:
        obj: an integer, the maximum number of hands that can be cleaned
    """
    from scipy.optimize import linprog

    c = [-30, -20]  # Coefficients of the objective function to maximize 30x + 20y

    A = [[40, 60], [50, 40], [-1, 0], [1, -1]]  # Coefficients of the constraints
    b = [available_water, available_alcohol, -liquid_constraint, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum number of hands that can be cleaned