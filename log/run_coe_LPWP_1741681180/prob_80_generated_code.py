from scipy.optimize import linprog

def prob_80(regular, emergency_fire):
    """
    Args:
        regular: an integer, representing the number of regular fire fighters.
        emergency_fire: an integer, representing the number of emergency fire fighters.
    
    Returns:
        obj: an integer, representing the minimum total cost of hiring fire fighters.
    """
    
    c = [300, 100]  # Coefficients of the objective function to minimize the total cost
    
    A = [[-10, -6], [300, 100]]  # Coefficients of the inequality constraints
    b = [-300, 7000]  # Right-hand side of the inequality constraints
    
    bounds = [(0, None), (0, None)]  # Bounds for x and y
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    return int(res.fun)