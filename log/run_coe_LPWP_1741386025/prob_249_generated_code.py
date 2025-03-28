def prob_249(retail_store, factory_outlet):
    """
    Args:
        retail_store: an integer indicating the number of retail stores
        factory_outlet: an integer indicating the number of factory outlets
    
    Returns:
        obj: an integer representing the objective value (number of stores)
    """
    
    from scipy.optimize import linprog
    
    # Coefficients of the objective function
    c = [1, 1]
    
    # Coefficients of the inequality constraints
    A = [[-200, -80], [6, 4]]
    b = [-1200, 50]
    
    # Bounds for variables
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    obj = res.fun  # Objective value
    
    return int(obj)