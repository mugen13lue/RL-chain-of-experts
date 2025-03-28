from scipy.optimize import linprog

def prob_194(small_trucks, large_trucks):
    """
    Args:
        small_trucks: an integer, representing the number of small trucks
        large_trucks: an integer, representing the number of large trucks
    Returns:
        obj: an integer, representing the maximum amount of snow that can be transported
    """
    c = [-30, -50]  # Coefficients of the objective function to be minimized (-30x - 50y)
    A = [[2, 4], [-1, 0], [0, -1], [-2, 1]]  # Coefficients of the inequality constraints
    b = [30, -10, -3, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum amount of snow that can be transported