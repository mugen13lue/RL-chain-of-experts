from scipy.optimize import linprog

def prob_77(dual, single):
    """
    Args:
        dual: an integer, representing the number of dual model stamping machines
        single: an integer, representing the number of single model stamping machines
    Returns:
        dual_purchase: an integer, representing the number of dual model stamping machines to purchase
        single_purchase: an integer, representing the number of single model stamping machines to purchase
    """
    c = [1, 1]  # Coefficients of the objective function to minimize x + y
    A = [[-50, -30], [20, 15], [-1, 1]]  # Coefficients of the inequality constraints
    b = [-300, 135, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

    return int(res.x[0]), int(res.x[1])