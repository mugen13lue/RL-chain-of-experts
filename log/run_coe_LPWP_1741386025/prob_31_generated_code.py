from scipy.optimize import linprog

def prob_31(premium_desktops, regular_desktops):
    """
    Args:
        premium_desktops: an integer, representing the number of premium desktops
        regular_desktops: an integer, representing the number of regular desktops
    Returns:
        obj: an integer, representing the objective value
    """
    c = [-500, -300]  # Coefficients of the objective function to maximize (500x + 300y)
    A = [[1, 1], [2000, 1000]]  # Coefficients of the inequality constraints
    b = [200, 300000]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraints)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = res.fun  # The objective value is the maximum value found by linprog

    return obj