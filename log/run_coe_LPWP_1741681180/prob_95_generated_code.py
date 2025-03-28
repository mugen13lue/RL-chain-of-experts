from scipy.optimize import linprog

def prob_95(heap_leaching, vat_leaching):
    """
    Args:
        heap_leaching: an integer, the proportion of lands that use heap leaching technique
        vat_leaching: an integer, the proportion of lands that use vat leaching technique
    Returns:
        obj: an float, the maximum daily production of rare earth oxide
    """
    c = [-3, -5]  # Coefficients of the objective function to minimize -3x - 5y
    A = [[1, 1], [10, 20], [8, 17]]  # Coefficients of the inequality constraints
    b = [100, 100, 90]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return -res.fun  # Return the negative of the minimum value as we are maximizing