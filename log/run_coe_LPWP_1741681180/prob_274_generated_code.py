from scipy.optimize import linprog

def prob_274(first_dose, second_dose):
    """
    Args:
        first_dose: an integer, represents the number of first-dose vaccines to be made
        second_dose: an integer, represents the number of second-dose vaccines to be made
    Returns:
        obj: an integer, represents the minimized amount of gelatine used
    """
    
    c = [0, 0, 1]  # Coefficients for the objective function [0, 0, 1] to minimize gelatine usage
    
    A = [[30, 65, 0],  # Coefficients for the Antibiotics constraint
         [20, 60, 0],  # Coefficients for the Gelatine constraint
         [-1, 1, 0],   # Coefficients for the First-dose requirement constraint
         [0, -1, 0]]   # Coefficients for the Second-dose minimum constraint
    
    b = [35000,  # Right-hand side for the Antibiotics constraint
         0,      # Right-hand side for the Gelatine constraint (to be optimized)
         0,      # Right-hand side for the First-dose requirement constraint
         -40]    # Right-hand side for the Second-dose minimum constraint
    
    res = linprog(c, A_ub=A, b_ub=b)
    
    return int(res.fun)  # Return the minimized amount of gelatine used