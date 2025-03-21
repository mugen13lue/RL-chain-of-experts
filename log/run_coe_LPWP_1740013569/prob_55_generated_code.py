def prob_55(windrower, hay_harvester):
    """
    Args:
        windrower: an integer,
        hay_harvester: an integer,
    Returns:
        obj: an integer,
    """
    from scipy.optimize import linprog

    c = [-10, -8]  # Coefficients of the objective function to be minimized

    A = [[10, 8], [5, 3], [2, 1]]  # Coefficients of the inequality constraints
    b = [200, 800, 300]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    obj = -res.fun  # Maximum amount of hay processed

    return obj