from scipy.optimize import linprog

def prob_233(high_volume, low_volume):
    """
    Args:
        high_volume: an integer, number of high-volume pipes
        low_volume: an integer, number of low-volume pipes
    Returns:
        obj: an integer, objective value
    """
    c = [1, 1]  # Coefficients for the objective function to minimize total number of pipes
    A = [[-10000, -5000], [12, 5], [-1, 0], [0, -1]]  # Coefficients for the constraints
    b = [-150000, 160, 0, -8]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun