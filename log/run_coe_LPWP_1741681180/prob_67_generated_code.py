from scipy.optimize import linprog

def prob_67(gas, electric):
    """
    Args:
        gas: an integer, number of gas grills
        electric: an integer, number of electric grills
    Returns:
        obj: an integer, minimum number of grills in the store
    """
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y

    A = [[-20, -30],  # Coefficients of the inequality constraints
         [20, 25],
         [-1, 1]]
    
    b = [-150, 140, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Minimum number of grills in the store