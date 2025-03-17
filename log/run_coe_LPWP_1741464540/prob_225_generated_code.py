from scipy.optimize import linprog

def prob_225(wide_pipes, narrow_pipes):
    """
    Args:
        wide_pipes: an integer representing the number of wide pipes
        narrow_pipes: an integer representing the number of narrow pipes
    Returns:
        obj: an integer representing the minimum total number of pipes required
    """
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    A = [[-25, -15], [-1, 0], [1, -1/3]]  # Coefficients of the constraints
    b = [-900, -5, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(wide_pipes, None), method='highs')
    return int(res.fun)  # Minimum total number of pipes required