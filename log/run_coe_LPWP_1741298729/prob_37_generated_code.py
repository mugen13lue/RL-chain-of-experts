from scipy.optimize import linprog

def prob_37(mango_cost, guava_cost):
    """
    Args:
        mango_cost: an integer, the cost of one mango
        guava_cost: an integer, the cost of one guava
    Returns:
        profit: an integer, the maximum profit
    """
    c = [-3, -4]  # Coefficients of the objective function to maximize profit (3x + 4y)
    A = [[5, 3], [3, 4]]  # Coefficients of the constraints
    b = [20000, 0]  # Right-hand side of the constraints
    bounds = [(100, 150), (0, None)]  # Bounds for the decision variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum profit