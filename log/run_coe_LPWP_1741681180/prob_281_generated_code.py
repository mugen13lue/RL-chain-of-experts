import numpy as np
from scipy.optimize import minimize

def prob_281(coconut_oil, lavender):
    """
    Args:
        coconut_oil: an integer, the number of units of coconut oil to be added
        lavender: an integer, the number of units of lavender to be added
    Returns:
        obj: an integer, the total amount of time
    """
    
    # Define the objective function to minimize
    def objective(x):
        return 0.7*x[0] + 0.9*x[1]
    
    # Define the constraints
    def constraint1(x):
        return x[0] - 300
    
    def constraint2(x):
        return x[0] + x[1] - 550
    
    def constraint3(x):
        return x[0] - 3*x[1]
    
    # Define the initial guess
    x0 = np.array([coconut_oil, lavender])
    
    # Define the bounds for the variables
    bounds = ((300, None), (0, 550))
    
    # Define the constraints
    cons = ({'type': 'eq', 'fun': constraint1},
            {'type': 'eq', 'fun': constraint2},
            {'type': 'eq', 'fun': constraint3})
    
    # Minimize the objective function subject to the constraints
    res = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)
    
    obj = res.fun
    
    return obj