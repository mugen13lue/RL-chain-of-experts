from scipy.optimize import linprog

def prob_125(anxiety_medication, anti_depressants):
    """
    Args:
        anxiety_medication: an integer (number of units of anxiety medication)
        anti_depressants: an integer (number of units of anti-depressants)
    Returns:
        total_time: an integer (total time it takes for the medication to be effective)
    """
    c = [3, 5]  # Coefficients of the objective function (3x + 5y)
    A = [[1, 1], [1, 0], [-2, 1]]  # Coefficients of the constraints
    b = [100, 30, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    total_time = res.fun  # Total time it takes for the medication to be effective

    return total_time