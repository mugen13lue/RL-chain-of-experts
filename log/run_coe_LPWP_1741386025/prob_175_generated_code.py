from scipy.optimize import linprog

def prob_175(seasonal, full_time):
    """
    Args:
        seasonal: an integer (number of seasonal volunteers),
        full_time: an integer (number of full-time volunteers)
    Returns:
        obj: an integer (total number of gifts that can be delivered)
    """
    c = [-5, -8]  # Coefficients of the objective function to maximize 5x + 8y
    A = [[2, 5], [-1, -0.3], [0, -0.1]]  # Coefficients of the inequality constraints
    b = [200, 0, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the negative of the optimized objective function value