from scipy.optimize import linprog

def prob_198(vans, cars):
    """
    Solve the voter transportation problem.

    Args:
        vans: an integer, number of vans
        cars: an integer, number of cars

    Returns:
        obj: an integer, total number of cars used
    """
    c = [0, 1]  # Coefficients for the objective function to minimize y
    A = [[6, 3], [-0.3, 0.7]]  # Coefficients for the constraints
    b = [200, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    return int(res.x[1])  # Return the optimal number of cars used