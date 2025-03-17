from scipy.optimize import linprog

def prob_43(Kebabs, Rice):
    """
    Args:
        Kebabs: an integer, the number of servings of Kebabs
        Rice: an integer, the number of servings of Rice
        
    Returns:
        obj: a float, the value of the objective function (minimized cost)
    """
    
    c = [3, 2]  # Cost coefficients
    A = [[-300, -200], [-4.5, -4]]  # Coefficients of constraints
    b = [-2200, -30]  # Right-hand side of constraints
    bounds = [(0, None), (0, None)]  # Non-negativity constraints
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    obj = res.fun  # Minimized cost
    
    return obj