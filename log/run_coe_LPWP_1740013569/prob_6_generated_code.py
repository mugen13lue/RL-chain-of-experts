def prob_6(tomatoes, potatoes):
    """
    Args:
        tomatoes: an integer, representing the number of hectares of tomatoes to plant
        potatoes: an integer, representing the number of hectares of potatoes to plant
    Returns:
        obj: an integer, representing the maximum profit
    """
    from scipy.optimize import linprog

    c = [-350, -600]  # Coefficients of the objective function to minimize (-1 * profit)
    A = [[1, 1], [1, 0], [0, 1], [-2, -1]]  # Coefficients of the inequality constraints
    b = [140, 140, 140, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(20, None), (30, None)])

    obj = -res.fun  # Maximum profit (negate the result from linprog as it minimizes)
    return int(obj)