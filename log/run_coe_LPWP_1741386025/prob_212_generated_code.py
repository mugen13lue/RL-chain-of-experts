from scipy.optimize import linprog

def prob_212():
    c = [2, 3]  # Coefficients of the objective function to minimize costs
    A = [[5, 4], [10, 15]]  # Coefficients of the constraints for iron and calcium
    b = [40, 50]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    
    return res.fun