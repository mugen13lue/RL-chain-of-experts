from scipy.optimize import linprog

def prob_270(smoothie, protein_bar):
    """
    Args:
        smoothie (int): Number of smoothies.
        protein_bar (int): Number of protein bars.

    Returns:
        obj (int): Objective value (maximum protein intake).
    """
    c = [-2, -7]  # Coefficients of the objective function Z = 2x + 7y to be minimized
    A = [[2, 7]]  # Coefficients of the inequality constraints
    b = [2000]    # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = -res.fun  # Maximum protein intake (negated because linprog minimizes by default)

    return obj