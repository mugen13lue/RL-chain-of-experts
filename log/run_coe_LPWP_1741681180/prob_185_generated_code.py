from scipy.optimize import linprog

def prob_185(labradors, golden_retrievers):
    """
    Args:
        labradors: an integer, the number of labradors used
        golden_retrievers: an integer, the number of golden retrievers used

    Returns:
        obj: an integer, the maximum number of newspapers that can be delivered
    """
    # Coefficients of the objective function
    c = [-7, -10]

    # Coefficients of the inequality constraints
    A = [[5, 6], [-1, 0.6], [0, -1], [1, 1]]
    b = [1500, 0, -50, 100]

    # Bounds for variables
    x_bounds = (0, None)
    y_bounds = (50, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values
    labradors = int(res.x[0])
    golden_retrievers = int(res.x[1])
    max_newspapers = -int(res.fun)

    return max_newspapers