from scipy.optimize import linprog

def prob_9(carrots, cucumbers):
    """
    Args:
        carrots: an integer, the number of carrots sold each month
        cucumbers: an integer, the number of cucumbers sold each month

    Returns:
        obj: an integer, the maximum profit
    """
    # Coefficients of the objective function
    c = [-0.75, -0.8]

    # Coefficients of the inequality constraints
    A = [[0.3, 0.5], [1, -1/3], [-1, 0], [1, 0]]
    b = [500, 0, -300, 500]

    # Bounds for variables
    x_bounds = (300, 500)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])

    # Extract the optimal values
    optimal_carrots = round(res.x[0])
    optimal_cucumbers = round(res.x[1])

    # Calculate the maximum profit
    max_profit = -res.fun

    return max_profit