from scipy.optimize import linprog

def prob_172():
    """
    Returns:
        obj: an integer
    """
    c = [2, 1.5]  # Coefficients of the objective function to minimize total time
    A = [[100, 40], [-1, -0.6]]  # Coefficients of the constraints
    b = [1200, 0]  # Right-hand side of the constraints
    bounds = [(0, 10), (0, None)]  # Bounds for the variables x (bus trips) and y (car trips)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = res.fun  # Optimal value of the objective function

    return obj