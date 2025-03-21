from scipy.optimize import linprog

def prob_239(limousine, bus):
    """
    Args:
        limousine: an integer, number of limousines used
        bus: an integer, number of buses used

    Returns:
        obj: an integer, total number of limousines and buses used
    """
    # Coefficients of the objective function
    c = [1, 1]

    # Coefficients of the inequality constraints
    A = [[-12, -18], [-0.3, 0.7]]

    # Right-hand side of the inequality constraints
    b = [-400, 0]

    # Bounds for variables
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values
    limousine = res.x[0]
    bus = res.x[1]

    return limousine + bus