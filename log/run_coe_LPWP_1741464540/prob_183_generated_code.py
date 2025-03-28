def prob_183(hot_air_balloon, gondola_lift):
    """
    Args:
        hot_air_balloon: an integer, represents the maximum number of hot air balloons rides
        gondola_lift: an integer, represents the maximum number of gondola lift rides
    Returns:
        obj: an integer, the minimized total pollution produced
    """
    
    from scipy.optimize import linprog
    
    # Coefficients of the objective function
    c = [10, 15]  # 10 units of pollution for hot air balloon, 15 units of pollution for gondola lift
    
    # Coefficients of the inequality constraints
    A = [[4, 6]]  # Number of visitors constraint
    
    # Bounds for the variables
    x_bounds = (0, hot_air_balloon)  # Maximum number of hot air balloon rides
    y_bounds = (0, gondola_lift)  # Maximum number of gondola lift rides
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, bounds=[x_bounds, y_bounds], method='highs')
    
    return int(res.fun)  # Return the minimized total pollution produced