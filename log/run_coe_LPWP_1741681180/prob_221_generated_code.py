def prob_221(personal_license, commercial_license):
    """
    Args:
        personal_license: an integer, representing the number of personal licenses
        commercial_license: an integer, representing the number of commercial licenses
    Returns:
        objective_value: an integer, representing the maximum profit
    """
    from scipy.optimize import linprog

    c = [-450, -1200]  # Coefficients of the objective function to be minimized
    A = [[1, 1], [550, 2000]]  # Coefficients of the inequality constraints
    b = [300, 400000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    objective_value = -res.fun  # Maximum profit is the negative of the minimum value found by linprog

    return int(objective_value)