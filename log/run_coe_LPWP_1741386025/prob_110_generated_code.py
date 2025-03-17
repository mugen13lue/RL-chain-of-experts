from scipy.optimize import linprog

def prob_110(syrup_1, syrup_2):
    """
    Args:
        syrup_1: an integer, the number of servings of syrup 1
        syrup_2: an integer, the number of servings of syrup 2
    Returns:
        obj: a float, the objective value (sugar intake)
    """
    c = [-0.5, -0.3]  # Corrected coefficients of the objective function to minimize sugar intake
    A = [[0.5, 0.2], [-0.4, -0.5]]  # Coefficients of the constraints
    b = [5, -4]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for the number of servings

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

    return res.fun