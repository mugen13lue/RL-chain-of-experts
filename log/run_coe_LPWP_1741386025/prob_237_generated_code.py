from scipy.optimize import linprog

def prob_237(pop, rnb, constraint1, constraint2, constraint3):
    """
    Args:
        pop: an integer, number of pop concerts
        rnb: an integer, number of R&B concerts
        constraint1: an integer, constraint for total audience size
        constraint2: an integer, constraint for total practice days
        constraint3: a float, constraint for maximum percentage of R&B concerts
    Returns:
        obj: an integer, total number of concerts
    """
    c = [1, 1]  # Coefficients of the objective function to minimize (x + y)
    A = [[-100, -240], [2, 4], [-0.6, 0.4]]  # Coefficients of the inequality constraints
    b = [-constraint1, constraint2, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun