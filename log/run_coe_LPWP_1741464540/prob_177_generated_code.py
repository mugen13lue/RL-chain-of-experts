def prob_177(tractor, car, twice):
    """
    Args:
        tractor: an integer, representing the number of tractors used
        car: an integer, representing the number of cars used
        twice: an integer, representing the minimum number of cars compared to tractors
    Returns:
        obj: an integer, representing the minimized total number of tractors and cars needed
    """
    
    # Import the optimization library
    from scipy.optimize import linprog
    
    # Coefficients of the objective function
    c = [1, 1]  # Coefficients for x (tractors) and y (cars)
    
    # Coefficients of the inequality constraints
    A = [[40, 20], [-1, -2]]  # Coefficients for corn weight and number of cars
    
    # Right-hand side of the inequality constraints
    b = [500, 0]  # 500 kg of corn needed and minimum number of cars constraint
    
    # Bounds for x and y (non-negativity constraint)
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    # Return the minimized total number of tractors and cars needed
    return int(res.x[0] + res.x[1])