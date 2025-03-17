from scipy.optimize import linprog

def prob_258():
    """
    Returns:
        obj: an integer, the objective value (amount of metal extracted)
    """
    c = [-5, -9]  # Coefficients of the objective function to maximize 5x + 9y
    A = [[8, 6], [3, 5]]  # Coefficients of the constraints
    b = [1500, 1350]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun * -1  # Return the negative of the objective value to maximize