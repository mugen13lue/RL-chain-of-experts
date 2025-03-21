def prob_112(demonstration_1, demonstration_2, _10, _20, _25, _12, _15, _18, _5, _3, _120, _100, _50):
    """
    Args:
        demonstration_1: an integer, represents the number of demonstration 1
        demonstration_2: an integer, represents the number of demonstration 2
        _10: an integer, represents the number of mint used in demonstration 1
        _20: an integer, represents the number of active ingredient used in demonstration 1
        _25: an integer, represents the amount of minty foam produced in demonstration 1
        _12: an integer, represents the number of mint used in demonstration 2
        _15: an integer, represents the number of active ingredient used in demonstration 2
        _18: an integer, represents the amount of minty foam produced in demonstration 2
        _5: an integer, represents the amount of black tar produced in demonstration 1
        _3: an integer, represents the amount of black tar produced in demonstration 2
        _120: an integer, represents the available amount of mint
        _100: an integer, represents the available amount of active ingredients
        _50: an integer, represents the maximum amount of black tar allowed

    Returns:
        obj: an integer, the objective value which is the amount of minty foam produced
    """
    from scipy.optimize import linprog

    c = [-25, -18]  # Coefficients of the objective function to be minimized

    A = [[10, 12], [20, 15], [5, 3]]  # Coefficients of the left-hand side of inequalities
    b = [120, 100, 50]  # Right-hand side of inequalities

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return -res.fun  # Return the negative of the optimized objective value to maximize it