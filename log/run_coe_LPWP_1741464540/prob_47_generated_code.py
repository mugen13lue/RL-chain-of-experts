from scipy.optimize import linprog

def prob_47(bagels, croissants, oven_hours, chef_hours):
    """
    Args:
        bagels: an integer, number of batches of bagels
        croissants: an integer, number of batches of croissants
        oven_hours: an integer, total oven hours used
        chef_hours: an integer, total chef hours used
    Returns:
        obj: an integer, maximum profit
    """
    c = [-20, -40]  # Coefficients of the objective function to maximize profit
    A = [[2, 1], [0.25, 2]]  # Coefficients of the constraints
    b = [oven_hours, chef_hours]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    max_profit = -res.fun  # Maximum profit is the negative of the minimum value returned by linprog

    return int(max_profit)