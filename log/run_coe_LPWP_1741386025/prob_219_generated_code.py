from scipy.optimize import linprog

def prob_219():
    """
    Returns:
        obj: an integer, representing the objective value (profit)
    """
    c = [-15, -17]  # Coefficients of the objective function to minimize (-15x - 17y)
    A = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1]]  # Coefficients of the inequality constraints
    b = [-40, -60, 140, 170, -200]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    return -res.fun  # Return the negative of the optimized profit value