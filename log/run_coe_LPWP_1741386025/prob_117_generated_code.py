def prob_117(burgers, pizza):
    """
    Args:
        burgers: an integer, the number of burgers
        pizza: an integer, the number of pizza slices
    Returns:
        obj: an integer, the objective value (cholesterol intake)
    """
    from scipy.optimize import linprog

    c = [0, 0, 1]  # Coefficients for the objective function [0, 0, 1] to minimize cholesterol intake
    A = [[-10, -8, 0], [-300, -250, 0], [12, 10, -1], [0, -1, 2]]  # Coefficients for the constraints
    b = [-130, -3000, 0, 0]  # RHS of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    obj = res.fun  # Minimized cholesterol intake

    return obj