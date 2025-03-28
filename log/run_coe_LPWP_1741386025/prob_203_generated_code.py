from scipy.optimize import linprog

def prob_203():
    """
    Returns:
        obj: a float, the maximum profit
    """
    c = [-7.5, -5]  # Coefficients of the objective function to be minimized
    A = [[600, 525], [10, 5]]  # Coefficients of the left-hand side of the inequalities
    b = [30000, 500]  # Right-hand side of the inequalities
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return -res.fun  # Return the maximum profit (negative because linprog minimizes by default)