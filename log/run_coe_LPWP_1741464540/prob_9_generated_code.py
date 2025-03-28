from scipy.optimize import linprog

def prob_9(carrots, cucumbers):
    """
    Args:
        carrots: an integer, the number of carrots sold each month
        cucumbers: an integer, the number of cucumbers sold each month

    Returns:
        obj: an integer, the maximum profit
    """
    c = [-0.75, -0.8]  # Coefficients of the objective function to be maximized (0.75x + 0.8y)
    A = [[0.3, 0.5], [1, -1/3]]  # Coefficients of the inequality constraints
    b = [500, 0]  # Right-hand side of the inequality constraints
    bounds = [(300, 500), (0, None)]  # Bounds for the decision variables

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res.fun  # Return the maximum value as we are maximizing the profit