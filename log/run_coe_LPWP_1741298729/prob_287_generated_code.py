from scipy.optimize import linprog

def prob_287(x, y):
    """
    Solves the problem of minimizing the total cost to the hospital.

    Args:
        x: Number of shifts using type II ambulance.
        y: Number of shifts using hospital van.
    
    Returns:
        obj: The objective value representing the total cost.
    """
    
    # Coefficients of the objective function
    c = [820, 550]
    
    # Coefficients of the inequality constraints
    A = [[20, 15], [1, 1], [-1, 0]]
    b = [320, x + y, 0.6*(x + y)]
    
    # Bounds for the variables
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    return res.fun