from scipy.optimize import linprog

def prob_256(trains, trams) -> int:
    """
    Args:
        trains: Number of trains (an integer).
        trams: Number of trams (an integer).

    Returns:
        obj: Total number of transportation units (an integer).
    """
    c = [1, 1]  # Coefficients of the objective function to minimize x + y
    A = [[-120, -30], [0, -1], [-2, 1]]  # Coefficients of the inequality constraints
    b = [-600, 0, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b)
    obj = res.fun  # Total number of transportation units required

    return int(obj)