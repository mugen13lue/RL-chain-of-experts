from scipy.optimize import linprog

def prob_285(wide_trail, narrow_trail):
    """
    Args:
        wide_trail: an integer, the number of wide trails
        narrow_trail: an integer, the number of narrow trails
    Returns:
        obj: an integer, the total amount of garbage produced
    """
    c = [6, 3]  # Coefficients of the objective function to minimize 6x + 3y
    A = [[1, 0], [1, 1]]  # Coefficients of the constraints x <= 3 and x + y <= 225
    b = [3, 225]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, 3), (0, None)])

    obj = res.fun  # Total amount of garbage produced

    return obj