from scipy.optimize import linprog

def prob_4(desk_lamps, night_lamps):
    """
    Args:
        desk_lamps: an integer, representing the number of desk lamps to be made
        night_lamps: an integer, representing the number of night lamps to be made
    Returns:
        obj: an integer, representing the maximum profit
    """
    
    # Coefficients of the objective function
    c = [-5, -8]  # Coefficients are negated as linprog minimizes the objective function
    
    # Coefficients of the inequality constraints
    A = [[-1, 0], [0, -1], [1, 1]]
    b = [-30, -50, 100]
    
    # Coefficients of the bounds
    x_bounds = (0, 150)
    y_bounds = (0, 180)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    # Calculate the maximum profit
    obj = -res.fun  # Negate the result to get the maximum profit
    
    return obj