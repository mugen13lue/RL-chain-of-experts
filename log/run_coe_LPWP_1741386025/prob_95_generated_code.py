from scipy.optimize import linprog

def prob_95(heap_leaching, vat_leaching):
    """
    Args:
        heap_leaching: an integer, the proportion of lands that use heap leaching technique
        vat_leaching: an integer, the proportion of lands that use vat leaching technique
    Returns:
        obj: an float, the maximum daily production of rare earth oxide
    """
    c = [-3, -5]  # Coefficients of the objective function to maximize 3x + 5y

    A = [[3, 5], [8, 17], [10, 20], [-1, -1]]  # Coefficients of the constraints
    b = [100, 90, 100, -1]  # Right-hand side of the constraints

    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun * -1  # Return the maximum daily production of rare earth oxide