from scipy.optimize import linprog

def prob_279(matcha_ice_cream, orange_sorbet):
    """
    Args:
        matcha_ice_cream: an integer representing the number of matcha ice cream desserts
        orange_sorbet: an integer representing the number of orange sorbet desserts
    Returns:
        obj: an integer representing the total amount of flavouring needed
    """
    
    c = [2, 4]  # Coefficients of the objective function (flavouring)
    A = [[2, 4], [4, 3], [-1, 0], [0, -1], [-0.85, -0.85]]  # Coefficients of the constraints
    b = [600, 550, 0, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun