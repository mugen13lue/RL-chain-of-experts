from scipy.optimize import linprog

def prob_173(van, minibus):
    """
    Args:
        van: an integer, represents the number of vans used
        minibus: an integer, represents the number of minibuses used
    Returns:
        obj: an integer, the total amount of pollution produced
    """
    # Coefficients of the objective function
    c = [7, 10]

    # Coefficients of the inequality constraints
    A = [[6, 10], [0, 1], [-1, 0]]
    b = [150, 10, 0]

    # Bounds for variables x and y
    x_bounds = (0, None)
    y_bounds = (0, 10)

    # Solving the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extracting the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    # Calculating the total amount of pollution produced
    obj = 7*x_opt + 10*y_opt

    return obj