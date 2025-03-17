from scipy.optimize import linprog

def prob_77():
    """
    Returns:
        dual_purchase: an integer, representing the number of dual model stamping machines to purchase
        single_purchase: an integer, representing the number of single model stamping machines to purchase
    """
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-50, -30], [20, 15], [-1, 0], [0, -1]]  # Coefficients for the constraints
    b = [-300, 135, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.x[0]), int(res.x[1])