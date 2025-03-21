from scipy.optimize import linprog

def prob_183(max_hot_air_balloon, max_gondola_lift):
    """
    Args:
        max_hot_air_balloon: an integer, represents the maximum number of hot air balloons rides
        max_gondola_lift: an integer, represents the maximum number of gondola lift rides
    Returns:
        obj: an integer, the minimized total pollution produced
    """
    
    # Coefficients of the objective function
    c = [10, 15]  # 10 units of pollution for hot air balloon, 15 units of pollution for gondola lift
    
    # Coefficients of the inequality constraints
    A = [[4, 6], [-1, 0], [0, -1]]  # Coefficients of the constraints
    b = [70, -max_hot_air_balloon, -max_gondola_lift]  # Right-hand side of the constraints
    
    # Bounds for the variables
    x_bounds = (0, max_hot_air_balloon)  # Bounds for hot air balloon rides
    y_bounds = (0, max_gondola_lift)  # Bounds for gondola lift rides
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    return res.fun