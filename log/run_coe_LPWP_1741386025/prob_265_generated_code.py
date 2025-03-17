from scipy.optimize import linprog

def prob_265(golf_carts, pull_carts):
    """
    Args:
        golf_carts: an integer, number of golf carts
        pull_carts: an integer, number of pull carts
    Returns:
        obj: an integer, the objective value
    """
    
    # Coefficients of the objective function
    c = [1, 1]
    
    # Coefficients of the inequality constraints
    A = [[4, 1], [-1, 0.6]]
    b = [80, 0]
    
    # Bounds for variables
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    obj = res.fun
    
    return obj