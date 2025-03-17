from scipy.optimize import linprog

def prob_270(smoothie, protein_bar):
    """
    Args:
        smoothie (int): Number of smoothies.
        protein_bar (int): Number of protein bars.

    Returns:
        obj (int): Objective value (maximum protein intake).
    """
    c = [-2, -7]  # Coefficients of the objective function to maximize 2x + 7y
    A = [[2, 7], [300, 250], [-2, 1]]  # Coefficients of the constraints
    b = [0, 2000, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    max_protein_intake = -res.fun  # Maximum protein intake

    return max_protein_intake