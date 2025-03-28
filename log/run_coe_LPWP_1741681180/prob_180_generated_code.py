from scipy.optimize import linprog

def prob_180(small, large):
    """
    Args:
        small: an integer, representing the number of small kegs
        large: an integer, representing the number of large kegs
    Returns:
        obj: an integer, representing the maximum amount of glacial water that can be transported
    """
    c = [-40, -100]  # Coefficients of the objective function to be minimized
    A = [[1, 0], [0, 1], [1, 1], [0, -1], [-2, 1]]  # Coefficients of the inequality constraints
    b = [30, 10, 25, -5, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, 30), (5, 10)], method='highs')
    obj = -res.fun  # Maximum amount of glacial water transported

    return obj