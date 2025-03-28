from scipy.optimize import linprog

def prob_269(runners, canoers):
    """
    Args:
        runners: an integer, number of runners
        canoers: an integer, number of canoers
    Returns:
        obj: an integer, amount of mail
    """
    # Coefficients of the objective function
    c = [-3, -10]  # Coefficients are negated for maximization

    # Coefficients of the inequality constraints
    A = [[3, 0], [0, 10], [4, 2], [-1, -0.33], [-1, 0]]

    # Right-hand side of the inequality constraints
    b = [200, 200, 200, 0, -4]

    # Bounds for variables
    x_bounds = (4, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values
    x_opt = res.x[0]
    y_opt = res.x[1]
    mail_delivered = -res.fun  # Negate the objective function value for maximization

    return int(mail_delivered)