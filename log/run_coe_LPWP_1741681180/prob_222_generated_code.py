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
    A = [[1, 1], [1, 0], [0, 1]]  # Coefficients of the constraints
    b = [100, 100, 80]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, 100))
    profit = -res.fun  # Maximum profit is the negative of the minimum value obtained by linprog

    return profit