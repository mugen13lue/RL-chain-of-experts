from scipy.optimize import linprog

def prob_153(old_vans, new_vans):
    """
    Args:
        old_vans: an integer, the number of old vans
        new_vans: an integer, the number of new vans
    Returns:
        obj: an integer, the total amount of pollution produced
    """
    c = [50, 30]  # Coefficients of the objective function to minimize pollution
    A = [[100, 80], [0, 1]]  # Coefficients of the constraints
    b = [5000, 30]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, 30)])

    return int(res.fun)  # Return the total amount of pollution produced