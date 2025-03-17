from scipy.optimize import linprog

def prob_67(gas, electric):
    """
    Args:
        gas: an integer, number of gas grills
        electric: an integer, number of electric grills
    Returns:
        gas: an integer, number of gas grills to be bought
        electric: an integer, number of electric grills to be bought
    """
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    A = [[-20, -30], [-20, -25], [-1, 0], [0, -1], [1, -1]]  # Coefficients of the constraints
    b = [-150, -140, 0, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    return int(res.x[0]), int(res.x[1])