from scipy.optimize import linprog

def prob_259(escalators, elevators):
    """
    Args:
        escalators: an integer, number of escalators
        elevators: an integer, number of elevators
    Returns:
        obj: an integer, total units of space taken
    """
    
    c = [5, 2]  # Coefficients of the objective function to minimize
    A = [[-20, -8], [-1, -3], [0, -1]]  # Coefficients of the inequality constraints
    b = [-400, -2, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    if res.success:
        obj = res.fun
    else:
        obj = None

    return obj