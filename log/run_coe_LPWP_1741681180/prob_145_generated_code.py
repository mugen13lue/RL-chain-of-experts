from scipy.optimize import linprog

def prob_145(process_1, process_2):
    """
    Args:
        process_1: an integer, number of times process 1 should be run
        process_2: an integer, number of times process 2 should be run

    Returns:
        obj: an integer, total time needed to minimize
    """
    
    c = [35, 50]  # Coefficients of the objective function to minimize
    A = [[-35, -50], [-12, -30], [50, 60]]  # Coefficients of the inequality constraints
    b = [-1200, -1200, 2000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun