from scipy.optimize import linprog

def prob_186(cows, elephants):
    """
    Args:
        cows: an integer, number of cows
        elephants: an integer, number of elephants
    Returns:
        obj: an integer, objective value
    """
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-20, -50], [-1, 0], [1, -2]]  # Coefficients for the constraints
    b = [-1000, 0, 0]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return int(res.fun)  # Return the minimum number of animals