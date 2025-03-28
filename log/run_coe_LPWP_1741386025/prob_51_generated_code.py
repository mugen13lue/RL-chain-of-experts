def prob_51(high_intensity, low_intensity):
    """
    Args:
        high_intensity: an integer representing the number of high intensity drills
        low_intensity: an integer representing the number of low intensity drills

    Returns:
        obj: an integer, representing the minimum total number of drills needed
    """
    
    # Integer Programming Model
    from scipy.optimize import linprog

    # Coefficients of the objective function
    c = [1, 1]

    # Coefficients of the inequality constraints
    A = [[50, 30], [50, 20], [-1, 0], [0, -1]]
    b = [800, 700, 0.4, -10]

    # Bounds for variables
    x_bounds = (0, None)
    y_bounds = (10, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    return int(res.fun)  # Minimum total number of drills needed