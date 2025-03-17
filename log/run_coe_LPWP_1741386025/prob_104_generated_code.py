def prob_104(orange_juice, apple_juice):
    """
    Args:
        orange_juice: an integer (number of orange juice boxes)
        apple_juice: an integer (number of apple juice boxes)
    Returns:
        objective_value: an integer (total vitamin D intake)
    """
    
    # Objective function coefficients
    obj_coeff = [-10, -12]  # Minimizing -10x - 12y is equivalent to maximizing 10x + 12y
    
    # Constraint coefficients
    constraint_coeff = [[10, 12], [8, 6], [-1, 0], [0, -3]]
    
    # Right-hand side of constraints
    rhs = [0, 300, -3, 0]
    
    # Bounds for variables
    bounds = [(3, None), (3, None)]
    
    from scipy.optimize import linprog
    
    # Solve the linear programming problem
    res = linprog(c=obj_coeff, A_ub=constraint_coeff, b_ub=rhs, bounds=bounds, method='highs')
    
    objective_value = -res.fun  # Maximum total vitamin D intake
    
    return objective_value