from scipy.optimize import linprog

def prob_105(cleansing_chemical, odor_removing_chemical):
    """
    Args:
        cleansing_chemical: an integer, the units of cleansing chemical used
        odor_removing_chemical: an integer, the units of odor-removing chemical used
    Returns:
        obj: an integer, the total time it takes for a house to be cleaned
    """
    c = [4, 6]  # Coefficients of the objective function to minimize total time
    A = [[-4, -6], [1, 0], [1, 1], [-2, 1]]  # Coefficients of the constraints
    b = [-600, -100, 300, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(100, None), (0, None)])
    return int(res.fun)