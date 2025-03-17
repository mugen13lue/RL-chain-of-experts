from scipy.optimize import linprog

def prob_49(turnips, pumpkins):
    """
    Args:
        turnips: an integer, represents the number of turnips to grow
        pumpkins: an integer, represents the number of pumpkins to grow
        
    Returns:
        obj: an integer, represents the objective value (revenue) to maximize
    """
    # Objective function coefficients
    c = [-300, -450]

    # Inequality constraints matrix
    A = [[1, 1], [50, 90], [80, 50]]
    b = [500, 40000, 34000]

    # Bounds for variables
    x_bounds = (0, 500)
    y_bounds = (0, 500)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values
    optimal_acres_turnips = res.x[0]
    optimal_acres_pumpkins = res.x[1]
    max_revenue = -res.fun

    print("Optimal acres of turnips:", optimal_acres_turnips)
    print("Optimal acres of pumpkins:", optimal_acres_pumpkins)
    print("Maximum revenue:", max_revenue)

    return max_revenue