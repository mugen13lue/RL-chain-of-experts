def prob_5(telecom, healthcare, three, _3, _1):
    """
    Args:
        telecom: an integer, amount invested in telecom
        healthcare: an integer, amount invested in healthcare
        three: an integer, constraint parameter
        _3: a float, telecom investment percentage
        _1: a float, healthcare investment percentage
    Returns:
        profit: a float, maximum profit
    """
    from scipy.optimize import linprog

    c = [-0.01, -0.03]  # Coefficients of the objective function to minimize (-0.01x - 0.03y)
    A = [[1, 1], [0, -1/3], [0, 1]]  # Coefficients of the inequality constraints
    b = [100000, 0, 70000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    return -res.fun  # Return the maximum profit