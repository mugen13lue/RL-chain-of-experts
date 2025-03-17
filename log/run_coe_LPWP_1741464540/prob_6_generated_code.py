from scipy.optimize import linprog

def prob_6(tomatoes, potatoes):
    """
    Args:
        tomatoes: an integer, representing the number of hectares of tomatoes to plant
        potatoes: an integer, representing the number of hectares of potatoes to plant
    Returns:
        obj: an integer, representing the maximum profit
    """
    
    # Coefficients of the objective function
    c = [-350, -600]  # We are maximizing profit, so we use negative values
    
    # Coefficients of the inequality constraints
    A = [[1, 1], [1, 0], [0, 1], [2, -1]]
    b = [140, 20, 30, 0]
    
    # Bounds for the variables
    x_bounds = (20, None)
    y_bounds = (30, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    return -res.fun  # Return the negative of the maximum profit