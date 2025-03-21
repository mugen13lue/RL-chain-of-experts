def prob_265(golf_carts, pull_carts):
    """
    Args:
        golf_carts: an integer, number of golf carts
        pull_carts: an integer, number of pull carts
    Returns:
        obj: an integer, the objective value
    """
    
    # Define the optimization problem
    from scipy.optimize import linprog
    
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    
    A = [[4, 1], [-1, -1]]  # Coefficients of the inequality constraints
    b = [80, 0]  # Right-hand side of the inequality constraints
    
    bounds = [(0, None), (0, None)]  # Bounds for x and y
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    obj = res.fun  # The optimal objective value
    
    return obj