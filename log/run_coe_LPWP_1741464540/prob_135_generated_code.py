from scipy.optimize import linprog

def prob_135(sulfate_units, ginger_units):
    """
    Args:
        sulfate_units: an integer, the amount of sulfate to be added to the shampoo.
        ginger_units: an integer, the amount of ginger to be added to the shampoo.
    Returns:
        obj: the total amount of time it takes for the mixture to be effective.
    """
    c = [0.5, 0.75]  # Coefficients of the objective function to minimize
    A = [[-1, 0], [-1, -1], [-2, 1]]  # Coefficients of the inequality constraints
    b = [-sulfate_units, -ginger_units, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b)
    return res.fun