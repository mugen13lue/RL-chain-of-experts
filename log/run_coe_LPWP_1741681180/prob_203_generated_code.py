from scipy.optimize import linprog

def prob_203(black_milk_tea, matcha_milk_tea):
    """
    Args:
        black_milk_tea: an integer, quantity of black milk tea to be made
        matcha_milk_tea: an integer, quantity of matcha milk tea to be made
    Returns:
        obj: a float, the maximum profit
    """
    
    # Coefficients of the objective function
    c = [-7.5, -5]  # Profit from black milk tea and matcha milk tea
    
    # Coefficients of the inequality constraints
    A = [[600, 525], [10, 5]]  # Coefficients of milk and honey for each type of milk tea
    b = [30000, 500]  # Available stock of milk and honey
    
    # Bounds for the variables
    x_bounds = (0, None)  # Non-negative quantities of milk tea
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds])
    
    # Calculate the maximum profit
    obj = -res.fun  # Negative because linprog minimizes the objective function
    
    return obj