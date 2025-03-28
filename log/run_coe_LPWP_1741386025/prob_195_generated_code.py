from scipy.optimize import linprog

def prob_195(carrier_pigeons, owls):
    """
    Args:
        carrier_pigeons: an integer, the number of carrier pigeons
        owls: an integer, the number of owls

    Returns:
        number_of_letters: an integer, the maximum number of letters that can be sent
    """
    c = [-2, -5]  # Coefficients of the objective function to maximize 2x + 5y
    A = [[3, 5], [-1, -0.6]]  # Coefficients of the inequality constraints
    b = [1000, -20]  # Right-hand side of the inequality constraints
    bounds = [(20, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    if res.success:
        return int(-res.fun)  # Maximum number of letters that can be sent
    else:
        return "No feasible solution found."