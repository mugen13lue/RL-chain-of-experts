from scipy.optimize import linprog

def prob_285(wide_trail, narrow_trail):
    """
    Args:
        wide_trail: an integer, the number of wide trails
        narrow_trail: an integer, the number of narrow trails
    Returns:
        obj: an integer, the total amount of garbage produced
    """
    
    # Coefficients of the objective function to minimize
    c = [6, 3]
    
    # Coefficients of the inequality constraints
    A = [[1, 0], [1, 1]]
    b = [3, 225]
    
    # Bounds for the variables
    x_bounds = (0, 3)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    obj = res.fun  # Total amount of garbage produced
    
    return obj