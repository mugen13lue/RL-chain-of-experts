from scipy.optimize import linprog

def prob_280(bus, personal_car):
    """
    Args:
        bus: an integer, represents the number of buses
        personal_car: an integer, represents the number of personal cars
    Returns:
        obj: an integer, the total number of vehicles
    """
    
    # Coefficients of the objective function
    c = [1, 1]  # Minimize x + y
    
    # Coefficients of the inequality constraints
    A = [[9, 4], [-1, 1], [0, -1]]  # Constraints: 9x + 4y >= 100, x >= y, y >= 5
    b = [100, 0, -5]  # RHS of the constraints
    
    # Bounds for variables
    x_bounds = (0, None)  # x >= 0
    y_bounds = (5, None)  # y >= 5
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    # Total number of vehicles scheduled
    obj = int(res.fun)
    
    return obj