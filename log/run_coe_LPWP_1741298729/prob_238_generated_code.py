from scipy.optimize import linprog

def prob_238():
    """
    Returns:
        obj: an integer, time spent baking
    """
    c = [12, 8]  # Coefficients for the objective function (baking time)
    A = [[12, 8], [5, 4], [0, 1], [-2, 1]]  # Coefficients for the constraints
    b = [10000, 4400, 200, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    if res.success:
        return int(res.fun)  # Return the minimum baking time
    else:
        return "No feasible solution found"