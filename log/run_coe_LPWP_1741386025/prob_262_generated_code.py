from scipy.optimize import linprog

def prob_262(kayak, motorboat, constraint1):
    """
    Args:
        kayak: an integer representing the number of kayaks to be used
        motorboat: an integer representing the number of motorboats to be used
        constraint1: an integer representing the minimum number of locals to be moved
    Returns:
        obj: an integer representing the amount of time needed to transport all the locals
    """
    
    # Coefficients of the objective function
    c = [5, 3]  # Coefficients for x (kayak trips) and y (motorboat trips)
    
    # Coefficients of the inequality constraints
    A = [[4, 5], [5, 3]]  # Coefficients for the constraints
    b = [constraint1, 25]  # Right-hand side of the constraints
    
    # Bounds for x and y (non-negative)
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    # Return the total amount of time needed to transport all the locals
    return res.fun