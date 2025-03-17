from scipy.optimize import linprog

def prob_23(elephants, tigers):
    """
    Args:
        elephants: an integer, the number of elephants to make
        tigers: an integer, the number of tigers to make
    Returns:
        profit: an integer, the maximum profit
    """
    c = [-5, -4]  # Coefficients of the objective function to be maximized (5x + 4y)
    A = [[50, 40], [20, 30]]  # Coefficients of the left-hand side of the inequalities
    b = [5000, 4000]  # Right-hand side of the inequalities
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return -res.fun  # Return the maximum profit found by linprog