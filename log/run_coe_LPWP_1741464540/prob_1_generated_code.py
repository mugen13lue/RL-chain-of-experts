from scipy.optimize import linprog

def prob_1(color_printers, bw_printers):
    """
    Args:
        color_printers: an integer representing the number of color printers
        bw_printers: an integer representing the number of black and white printers
    
    Returns:
        obj: an integer representing the optimal objective value (profit)
    """
    c = [200, 70]  # Corrected coefficients of the objective function to be maximized (200x + 70y)
    A = [[1, 0], [0, 1], [1, 1]]  # Coefficients of the inequality constraints
    b = [20, 30, 35]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    obj = res.fun  # Maximum profit is the value obtained by linprog

    return obj