from scipy.optimize import linprog

def prob_254(large_bags, tiny_bags):
    """
    Args:
        large_bags: an integer, the number of large bags of grain
        tiny_bags: an integer, the number of tiny bags of grain
    Returns:
        obj: an integer, the maximum amount of grain in weight
    """
    
    # Coefficients of the objective function
    c = [-25, -6]  # Coefficients are negated for maximization

    # Coefficients of the inequality constraints
    A = [[4, 1.5], [-1, 2], [0, -1]]  # Energy Constraint, Large Bags Constraint, Tiny Bags Constraint
    b = [110, 0, -20]  # Right-hand side of the inequality constraints

    # Bounds for variables
    x_bounds = (0, None)  # Large bags must be non-negative
    y_bounds = (20, None)  # At least 20 tiny bags

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = int(res.x[0])
    y_opt = int(res.x[1])

    # Calculate the maximum amount of grain in weight
    obj = -res.fun  # Negate the objective value back to positive

    return obj