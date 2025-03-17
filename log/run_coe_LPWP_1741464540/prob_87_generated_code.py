from scipy.optimize import linprog

def prob_87(manual_slicers, automatic_slicers, constraint1, constraint2, constraint3):
    """
    Args:
        manual_slicers: an integer, represents the number of manual slicers
        automatic_slicers: an integer, represents the number of automatic slicers
        constraint1: a string, represents the constraint "manual_slicers <= automatic_slicers"
        constraint2: a string, represents the constraint "5 * manual_slicers + 8 * automatic_slicers >= 50"
        constraint3: a string, represents the constraint "3 * manual_slicers + 6 * automatic_slicers <= 35"
    Returns:
        obj: an integer, represents the minimum total number of slicers
    """
    
    c = [1, 1]  # Coefficients of the objective function to minimize x + y
    
    A = [[-1, 0],  # Coefficients of the constraint manual_slicers <= automatic_slicers
         [-5, -8],  # Coefficients of the constraint 5 * manual_slicers + 8 * automatic_slicers >= 50
         [3, 6]]    # Coefficients of the constraint 3 * manual_slicers + 6 * automatic_slicers <= 35
    
    b = [0, -50, 35]  # Right-hand side of the constraints
    
    res = linprog(c, A_ub=A, b_ub=b)
    
    return res.fun