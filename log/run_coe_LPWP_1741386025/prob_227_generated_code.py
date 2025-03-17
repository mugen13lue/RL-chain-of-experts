from scipy.optimize import linprog

def prob_227(subsoil, topsoil):
    """
    Args:
        subsoil: an integer, number of bags of subsoil
        topsoil: an integer, number of bags of topsoil

    Returns:
        obj: an integer, the minimized amount of water required to hydrate the garden bed
    """
    c = [10, 6]  # Coefficients of the objective function to minimize 10x + 6y
    A = [[10, 6], [0, -1], [-0.3, -0.7]]  # Coefficients of the constraints
    b = [150, -10, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Return the minimized amount of water required