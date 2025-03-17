from scipy.optimize import linprog

def prob_33(long_desks, short_desks):
    """
    Args:
        long_desks: an integer (number of long desks),
        short_desks: an integer (number of short desks)
        
    Returns:
        objective_value: a float (objective value, seating availability)
    """
    c = [-6, -2]  # Coefficients of the objective function to maximize seating availability
    A = [[10, 4]]  # Coefficients of the constraints (total square feet)
    b = [200]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for the number of desks
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    objective_value = -res.fun  # Maximum seating availability
    
    return objective_value