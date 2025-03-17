from scipy.optimize import linprog

def prob_178(bike, car):
    """
    Args:
        bike: an integer, represents the number of bikes
        car: an integer, represents the number of cars
    Returns:
        obj: an integer, the objective value
    """
    
    # Define the coefficients of the objective function
    c = [1, 0]  # Minimize y (number of bikes)
    
    # Define the inequality constraints matrix
    A = [[3, 5], [-0.6, 1]]  # Coefficients of the constraints
    
    # Define the inequality constraints vector
    b = [500, 0]  # RHS of the constraints
    
    # Define the bounds for variables
    x_bounds = (0, None)  # x (number of cars) >= 0
    y_bounds = (0, None)  # y (number of bikes) >= 0
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    obj = res.fun  # Objective value (minimum number of bikes needed)
    
    return obj