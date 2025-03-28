from scipy.optimize import linprog

def prob_168(scooter, rickshaw):
    """
    Args:
        scooter: an integer, number of scooters used
        rickshaw: an integer, number of rickshaws used

    Returns:
        obj: an integer, total number of scooters used
    """
    c = [1, 0]  # Coefficients for the objective function (minimize x)
    A = [[2, 3], [-0.4, -0.6]]  # Coefficients for the inequality constraints
    b = [300, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b)
    obj = int(res.x[0])  # Total number of scooters used

    return obj