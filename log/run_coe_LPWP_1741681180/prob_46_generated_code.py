from scipy.optimize import linprog

def prob_46(vegetable, fruits):
    """
    Solve the problem to minimize cost using linear programming.

    Args:
        vegetable: an integer, representing the number of servings of vegetables
        fruits: an integer, representing the number of servings of fruits

    Returns:
        obj: an integer, representing the objective value (cost)
    """
    c = [3, 5]  # Cost coefficients
    A = [[-2, -4], [-3, -1]]  # Coefficients for the constraints
    b = [-20, -30]  # RHS of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    obj = res.fun

    return obj