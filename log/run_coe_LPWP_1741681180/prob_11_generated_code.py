from scipy.optimize import linprog

def prob_11(condos, detached_houses):
    """
    Args:
        condos: a float, representing the amount invested in condos
        detached_houses: a float, representing the amount invested in detached houses
    
    Returns:
        obj: a float, representing the maximum profit earned from the investment
    """
    c = [-0.5, -1]  # Coefficients of the objective function to be minimized (-0.5x - y)
    A = [[1, 1], [-0.8, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [760000, 0, -20000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])
    obj = -res.fun  # Maximum profit is the negative of the minimum value obtained by linprog

    return obj