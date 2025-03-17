from scipy.optimize import linprog

def prob_115(fertilizer, seeds):
    """
    Args:
        fertilizer: an integer, the number of units of fertilizer
        seeds: an integer, the number of units of seeds
    Returns:
        obj: an integer, the total time it takes for the lawn to be ready
    """
    c = [0.5, 1.5]  # Coefficients of the objective function
    A = [[1, 1], [-1, 0], [-1, -2]]  # Coefficients of the constraints
    b = [300, -50, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(50, None), (0, None)])

    obj = res.fun  # Total time it takes for the lawn to be ready

    return obj