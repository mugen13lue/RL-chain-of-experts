from scipy.optimize import linprog

def prob_185(labradors, golden_retrievers):
    """
    Args:
        labradors: an integer, the number of labradors used
        golden_retrievers: an integer, the number of golden retrievers used

    Returns:
        obj: an integer, the maximum number of newspapers that can be delivered
    """
    c = [-7, -10]  # Coefficients of the objective function to maximize (7x + 10y)
    A = [[5, 6], [0, -1], [-0.4, 1]]  # Coefficients of the inequality constraints
    b = [1500, -50, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Convert the negative optimal value to positive