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

    c = [-30, -20]  # Coefficients of the objective function to be minimized (-30x - 20y)
    A = [[40, 60], [50, 40], [-1, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [available_water, available_alcohol, -liquid_constraint, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return -int(res.fun)  # Return the negative of the optimized objective function value as we are maximizing it