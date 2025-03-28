def prob_31(premium_desktops, regular_desktops):
    """
    Args:
        premium_desktops: an integer, representing the number of premium desktops
        regular_desktops: an integer, representing the number of regular desktops
    Returns:
        obj: an integer, representing the objective value
    """
    from scipy.optimize import linprog

    c = [-500, -300]  # Coefficients of the objective function to be minimized
    A = [[1, 1], [2000, 1000]]  # Coefficients of the inequality constraints
    b = [200, 300000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return -res.fun  # Return the negative of the minimum value as we are maximizing profit