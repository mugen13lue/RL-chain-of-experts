from scipy.optimize import linprog

def prob_99(peach_flavored_candy, cherry_flavored_candy):
    """
    Args:
        peach_flavored_candy: an integer, the number of peach flavored candy packs
        cherry_flavored_candy: an integer, the number of cherry flavored candy packs

    Returns:
        obj: an integer, the minimal amount of special syrup used
    """
    
    c = [5, 4]  # Coefficients of the objective function to minimize 5x + 4y
    A = [[-3, 0], [0, -5], [-1, 1], [0.3, -0.3]]  # Coefficients of the constraints
    b = [-3000, -4000, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)