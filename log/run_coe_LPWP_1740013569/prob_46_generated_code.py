from scipy.optimize import linprog

def prob_46():
    """
    Solve the problem to minimize cost.

    Returns:
        obj: an integer, representing the objective value (cost)
    """
    # Coefficients of the objective function
    c = [3, 5]

    # Coefficients of the inequality constraints
    A = [[-2, -4], [-3, -1]]
    b = [-20, -30]

    # Bounds for variables (x >= 0, y >= 0)
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values
    optimal_servings = res.x
    optimal_cost = res.fun

    return optimal_cost