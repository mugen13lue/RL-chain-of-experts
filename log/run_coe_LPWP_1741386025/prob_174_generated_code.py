from scipy.optimize import linprog

def prob_174(small_bins, large_bins):
    """
    Solve the recycling problem and maximize the total amount of recycling material that can be collected.

    Args:
        small_bins: an integer, number of small bins
        large_bins: an integer, number of large bins

    Returns:
        obj: an integer, total amount of recycling material
    """
    
    # Coefficients of the objective function
    c = [-25, -60]

    # Coefficients of the inequality constraints
    A = [[2, 5], [-1, 0], [0, -1], [-3, 1]]
    b = [100, -10, -4, 0]

    # Bounds for variables
    x_bounds = (10, None)
    y_bounds = (4, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])

    # Extract the optimal values
    x_opt = res.x[0]
    y_opt = res.x[1]
    total_recycling = -res.fun

    return round(total_recycling)