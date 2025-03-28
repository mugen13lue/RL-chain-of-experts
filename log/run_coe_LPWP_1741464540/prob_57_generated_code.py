from scipy.optimize import linprog

def prob_57(cash_based, card_only):
    """
    Args:
        cash_based: an integer, number of cash-based machines
        card_only: an integer, number of card-only machines
    Returns:
        obj: an integer, the objective value
    """
    
    # Coefficients of the objective function
    c = [1, 1]
    
    # Coefficients of the inequality constraints
    A = [[-20, -30], [4, 5], [-1, 1]]
    b = [-500, 90, 0]
    
    # Bounds for the variables
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    obj = res.fun
    
    return obj