def prob_25(apartments, townhouses):
    """
    
    Args:
        apartments: an integer, amount of money invested in apartments
        townhouses: an integer, amount of money invested in townhouses
    
    Returns:
        profit: an integer, maximum profit
    """
    from scipy.optimize import linprog

    c = [-0.10, -0.15]  # Coefficients of the objective function to be minimized
    A = [[1, 1], [1, -0.5]]  # Coefficients of the inequality constraints
    b = [600000, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, 200000), (0, None)])

    return -res.fun  # Maximum profit is the negative of the minimum value found by linprog