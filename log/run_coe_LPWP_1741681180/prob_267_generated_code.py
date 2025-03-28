from scipy.optimize import linprog

def prob_267(basketballs, footballs):
    """
    Args:
        basketballs: an integer, representing the number of basketballs
        footballs: an integer, representing the number of footballs
        
    Returns:
        obj: an integer, representing the total number of sports equipment produced
    """
    
    # Coefficients of the objective function
    c = [-1, -1]  # Maximize Z = -x - y
    
    # Coefficients of the inequality constraints
    A = [[5, 3], [1, 2], [-1, 3], [0, -1]]
    b = [1500, 750, 0, -50]
    
    # Bounds for x and y
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    obj = -res.fun  # Maximum total number of sports equipment produced
    
    return int(obj)