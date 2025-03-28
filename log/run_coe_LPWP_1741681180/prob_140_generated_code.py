from scipy.optimize import linprog

def prob_140(Beam_1, Beam_2):
    """
    Args:
        Beam_1: an integer, the number of minutes of Beam 1 used
        Beam_2: an integer, the number of minutes of Beam 2 used

    Returns:
        obj: an integer, the minimized total radiation received by the pancreas
    """
    
    c = [0.3, 0.2]  # Coefficients for the objective function to minimize total radiation received by the pancreas
    A = [[-0.6, -0.4], [0.2, 0.1]]  # Coefficients for the inequality constraints
    b = [-3, 4]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun