from scipy.optimize import linprog

def prob_84(experiment_alpha, experiment_beta):
    """
    Args:
        experiment_alpha: an integer, represents the number of times to conduct experiment alpha
        experiment_beta: an integer, represents the number of times to conduct experiment beta
    Returns:
        obj: an integer, the maximum amount of electricity produced
    """
    
    # Coefficients of the objective function to be maximized
    c = [-8, -10]  # Coefficients are negated for maximization
    
    # Coefficients of the inequality constraints
    A = [[3, 5], [5, 4]]  # Coefficients of metal and acid for each experiment
    b = [800, 750]  # Available units of metal and acid
    
    # Bounds for the variables
    x_bounds = (0, None)  # x >= 0
    y_bounds = (0, None)  # y >= 0
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    # Extract the maximum amount of electricity produced
    obj = -res.fun  # Negate the result back to get the actual maximum
    
    return obj