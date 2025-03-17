from scipy.optimize import linprog

def prob_73(regular, hybrid):
    """
    Args:
        regular: an integer, number of regular vans
        hybrid: an integer, number of hybrid vans
    Returns:
        regular_vans: an integer, optimal number of regular vans
        hybrid_vans: an integer, optimal number of hybrid vans
    """
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-500, -300], [200, 100]]  # Coefficients for the inequality constraints
    b = [-20000, 7000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.x[0]), int(res.x[1])