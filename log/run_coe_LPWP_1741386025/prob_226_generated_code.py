from scipy.optimize import linprog

def prob_226():
    """
    Solve the transportation problem.
    
    Returns:
        obj: an integer, total number of workers
    """
    # Coefficients of the objective function
    c = [2, 4]

    # Coefficients of the inequality constraints
    A = [[-5, -7], [-2, -4], [0, -1], [0.4, -0.4]]

    # Right-hand side of the inequality constraints
    b = [-100, -12, 0, 0]

    # Bounds for variables x and y
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    # Calculate the total number of workers
    total_workers = 2*x_opt + 4*y_opt

    return total_workers