def prob_287(total_shifts):
    """
    Solves the problem of minimizing the total cost to the hospital.

    Args:
        total_shifts: Total number of shifts to schedule.
    
    Returns:
        obj: The objective value representing the total cost.
    """
    from scipy.optimize import linprog

    # Coefficients of the objective function
    c = [820, 550]

    # Coefficients of the inequality constraints
    A = [[20, 15], [1, 1], [-1, 0]]
    b = [320, total_shifts, 0.6*total_shifts]

    # Bounds for the variables
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    return res.fun