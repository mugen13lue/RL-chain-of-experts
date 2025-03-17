from scipy.optimize import linprog

def prob_175(seasonal, full_time):
    """
    Args:
        seasonal: an integer (number of seasonal volunteers),
        full_time: an integer (number of full-time volunteers)
    Returns:
        obj: an integer (total number of gifts that can be delivered)
    """
    
    # Coefficients of the objective function
    c = [-5, -8]  # Coefficients are negated for maximization

    # Coefficients of the inequality constraints
    A = [[2, 5], [-1, -0.3], [0, -1]]
    b = [200, 0, -10]

    # Bounds for x and y (non-negativity constraints)
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solving the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extracting the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    # Calculating the total number of gifts delivered
    total_gifts = -res.fun  # Objective function value is negated

    return round(total_gifts)