import numpy as np
from scipy.optimize import linprog

def prob_60():
    """
    Returns:
        number_of_snow_removers: an integer, the objective value (i.e., minimized number of snow removers)
    """
    
    # Set up the coefficients of the constraints
    A = np.array([[120, 250], [6, 10]])
    b = np.array([6500, 300])
    
    # Solve the linear programming problem
    res = linprog(c=[1, 1], A_ub=A, b_ub=b, bounds=(0, None))
    
    return int(res.x[0] + res.x[1])

# Example usage
print(prob_60())  # Output should be the minimized number of snow removers