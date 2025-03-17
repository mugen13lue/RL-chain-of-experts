from scipy.optimize import linprog

def prob_281(coconut_oil, lavender):
    """
    Args:
        coconut_oil: an integer, the number of units of coconut oil to be added
        lavender: an integer, the number of units of lavender to be added
    Returns:
        obj: an integer, the total amount of time
    """
    c = [0.7, 0.9]  # Coefficients of the objective function (time)
    A = [[-1, 0], [-1, -1], [0, -3]]  # Coefficients of the inequality constraints
    b = [-300, -550, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])

    return res.fun