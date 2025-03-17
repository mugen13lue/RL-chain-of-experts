def prob_117(burgers, pizza):
    """
    Args:
        burgers: an integer, the number of burgers
        pizza: an integer, the number of pizza slices
    Returns:
        obj: an integer, the objective value (cholesterol intake)
    """
    obj = 12 * burgers + 10 * pizza  # Objective function to minimize cholesterol intake

    # Solve the optimization problem
    from scipy.optimize import linprog
    c = [12, 10]  # Coefficients of the objective function
    A = [[-10, -8], [-300, -250], [12, 10]]  # Coefficients of the constraints
    b = [-130, -3000, 0]  # Right-hand side of the constraints
    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    obj = res.fun  # Optimal value of the objective function
    return obj