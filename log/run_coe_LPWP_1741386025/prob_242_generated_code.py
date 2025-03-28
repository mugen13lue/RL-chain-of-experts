from scipy.optimize import linprog

def prob_242(x, y):
    """
    Args:
        x: an integer, the number of bowls of salmon to eat
        y: an integer, the number of bowls of eggs to eat
    Returns:
        obj: a float, the objective value (sodium intake)
    """
    c = [0, 0, 1]  # Coefficients for the objective function [0, 0, 1] to minimize sodium intake
    A = [[-300, -200, 0], [-15, -8, 0], [0, -1, -0.4], [80, 20, -1]]  # Coefficients for the constraints
    b = [-2000, -90, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    obj = res.fun  # Optimal value of the objective function

    return obj