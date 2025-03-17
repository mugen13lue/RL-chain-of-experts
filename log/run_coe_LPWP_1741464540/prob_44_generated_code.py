from scipy.optimize import linprog

def prob_44():
    # Coefficients of the objective function
    c = [-200, -300]  # We are maximizing profit, so we use negative values

    # Coefficients of the inequality constraints
    A = [[2, 4], [3, 5]]  # Design team and engineering team hours constraints
    b = [5000, 6000]  # Available hours for design and engineering teams

    # Bounds for the variables (non-negativity constraints)
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    return int(x_opt), int(y_opt)