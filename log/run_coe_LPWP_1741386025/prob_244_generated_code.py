from scipy.optimize import linprog

def prob_244(chop_saw, steel_cutter, cut_limitation, waste_limitation):
    """
    Args:
        chop_saw: an integer, the number of chop saws
        steel_cutter: an integer, the number of steel cutters
        cut_limitation: an integer, the cut limitation in pounds
        waste_limitation: an integer, the waste limitation in units
    Returns:
        obj: an integer, the objective value
    """
    
    # Coefficients of the objective function
    c = [1, 1]  # Minimize x + y
    
    # Coefficients of the inequality constraints
    A = [[-25, -5], [25, 3]]
    b = [-cut_limitation, waste_limitation]
    
    # Bounds for variables
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    return res.fun