from scipy.optimize import linprog

def prob_190(small_crates, large_crates):
    """
    Args:
        small_crates: an integer (number of small crates),
        large_crates: an integer (number of large crates)

    Returns:
        obj: an integer (total number of grapes)
    """
    c = [-200, -500]  # Coefficients of the objective function to be minimized
    A = [[-1, 0], [0, -1], [1, 1], [-3, -1]]  # Coefficients of the inequality constraints
    b = [-100, -50, 60, -10]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, 100), (10, 50)])
    total_grapes = -res.fun  # Maximum total number of grapes transported

    return total_grapes