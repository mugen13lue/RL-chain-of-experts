def prob_48(factory_1, factory_2, constraint_1, constraint_2, constraint_3):
    """
    Args:
        factory_1: an integer (number of hours for factory 1),
        factory_2: an integer (number of hours for factory 2),
        constraint_1: an integer (limit for constraint 1),
        constraint_2: an integer (limit for constraint 2),
        constraint_3: an integer (limit for constraint 3),
    Returns:
        cost: an integer (the minimized cost of production),
    """
    from scipy.optimize import linprog

    c = [300, 600]  # Coefficients of the objective function to minimize cost
    A = [[-5, -10], [-6, -10], [-3, 0]]  # Coefficients of the inequality constraints
    b = [-constraint_1, -constraint_2, -constraint_3]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    cost = res.fun  # Minimized cost of production

    return int(cost)