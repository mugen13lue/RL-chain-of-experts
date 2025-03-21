def prob_91(A, B, _30, _100, _50, _120):
    """
    Args:
        A: an integer
        B: an integer
        _30: an integer
        _100: an integer
        _50: an integer
        _120: an integer
    Returns:
        obj: an integer
    """
    from scipy.optimize import linprog

    c = [1, 1]  # Coefficients of the objective function to minimize x + y

    A_eq = [[30, 50], [-100, -120]]  # Coefficients of the equality constraints
    b_eq = [1000, -3000]  # Values of the equality constraints

    A_ub = [[-1, -1], [0, -1], [-1, 0]]  # Coefficients of the inequality constraints
    b_ub = [-5, 0, 0]  # Values of the inequality constraints

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=(0, None))

    obj = res.fun  # Optimal value of the objective function

    return int(obj)