from scipy.optimize import linprog

def prob_132(table_1, table_2):
    """
    Args:
        table_1: an integer, number of tables set up at table 1
        table_2: an integer, number of tables set up at table 2
    Returns:
        max_slime: an integer, maximum amount of slime produced
    """
    c = [-4, -5]  # Coefficients of the objective function to maximize 4x + 5y
    A = [[3, 8], [5, 6], [2, 4]]  # Coefficients of the constraints
    b = [100, 90, 30]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Non-negative bounds for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    max_slime = -res.fun  # Maximum amount of slime produced

    return max_slime