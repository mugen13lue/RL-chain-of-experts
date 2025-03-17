from scipy.optimize import linprog

def prob_8(clothing_company, tech_company):
    """
    Args:
        clothing_company: an integer, representing the investment in the clothing company.
        tech_company: an integer, representing the investment in the tech company.
    Returns:
        obj: an integer, representing the maximum profit.
    """
    # Coefficients of the objective function
    c = [-0.07, -0.10]  # We want to maximize profit, so we negate the coefficients

    # Coefficients of the inequality constraints
    A = [[1, 1], [-4, -1], [0, -1]]  # x + y <= 3000, x >= 4y, y <= 500
    b = [3000, 0, -500]

    # Bounds for the variables
    x_bounds = (0, None)  # x >= 0
    y_bounds = (0, None)  # y >= 0

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    # Calculate the maximum profit
    max_profit = -res.fun

    return max_profit