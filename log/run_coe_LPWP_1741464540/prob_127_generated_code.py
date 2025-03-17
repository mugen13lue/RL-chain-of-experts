from scipy.optimize import linprog

def prob_127(cashews, almonds, _200, _20, _300, _25, twice, _15, _12, _10000, _800):
    """
    Args:
        cashews: an integer
        almonds: an integer
        _200: an integer
        _20: an integer
        _300: an integer
        _25: an integer
        twice: an integer
        _15: an integer
        _12: an integer
        _10000: an integer
        _800: an integer
    Returns:
        obj: an integer
    """
    # Coefficients of the objective function (minimize fat intake)
    c = [_15, _12]

    # Coefficients of the inequality constraints (calorie and protein constraints)
    A = [[-_200, -_300], [-_20, -_25]]
    b = [-_10000, -_800]

    # Coefficients of the equality constraint (at least twice as many servings of almonds as cashews)
    A_eq = [[-1, -1]]
    b_eq = [0]

    # Bounds for the number of servings of almonds and cashews
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal number of servings of almonds and cashews
    servings_almonds = res.x[0]
    servings_cashews = res.x[1]

    return servings_almonds, servings_cashews