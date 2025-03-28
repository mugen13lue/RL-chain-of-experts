from scipy.optimize import linprog

def prob_222(strawberry_cookie, sugar_cookie):
    """
    Args:
        strawberry_cookie: an integer, the number of strawberry cookies to make
        sugar_cookie: an integer, the number of sugar cookies to make

    Returns:
        profit: a float, the maximum profit
    """
    c = [-5.5, -12]  # Coefficients of the objective function to minimize (-5.5x1 - 12x2)
    A = [[1, 1]]  # Coefficients of the inequality constraints
    b = [100]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    max_profit = -res.fun  # The optimized value gives the negative of the maximum profit

    return max_profit