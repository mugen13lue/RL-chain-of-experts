from scipy.optimize import linprog

def prob_75(traditional_machine, modern_machine):
    """
    Args:
        traditional_machine: an integer, represents the number of acres to be used for traditional machine
        modern_machine: an integer, represents the number of acres to be used for modern machine
    Returns:
        obj: an integer, represents the maximum amount of tea leaves that can be picked
    """
    c = [-30, -40]  # Coefficients of the objective function to maximize (negative because linprog minimizes)
    A = [[30, 40], [10, 15], [20, 15]]  # Coefficients of the constraints
    b = [500, 6000, 9000]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum amount of tea leaves that can be picked