from scipy.optimize import linprog

def prob_213(regular_handbags, premium_handbags):
    """
    Args:
        regular_handbags (int): Number of regular handbags to sell
        premium_handbags (int): Number of premium handbags to sell

    Returns:
        profit (int): Maximum monthly profit
    """
    c = [-30, -180]  # Coefficients of the objective function to minimize (-profit)
    A = [[200, 447], [1, 1]]  # Coefficients of the inequality constraints
    b = [250000, 475]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])
    profit = -res.fun  # Maximum profit is the negative of the minimum value found by linprog

    return int(profit)