def prob_228(densely_seated_one, loosely_seated_one):
    """
    Solve the ski lifts problem to minimize the total number of ski lifts needed.

    Args:
        densely_seated_one: Number of densely-seated ski lifts (integer).
        loosely_seated_one: Number of loosely-seated ski lifts (integer).

    Returns:
        total_lifts: Total number of ski lifts needed (integer).
    """
    from scipy.optimize import linprog

    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y

    A = [[-1, 0], [0, -1], [-45, -20], [30, 22]]  # Coefficients of the constraints
    b = [0, -5, -1000, 940]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    total_lifts = int(res.x[0] + res.x[1])  # Total number of ski lifts needed

    return total_lifts