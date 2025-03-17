from scipy.optimize import linprog

def prob_26(Zodiac, Sunny):
    """
    Args:
        Zodiac: an integer, number of pills of Zodiac
        Sunny: an integer, number of pills of Sunny
    Returns:
        obj: an integer, objective value
    """
    c = [1, 3]  # Coefficients of the objective function (costs of Zodiac and Sunny)
    A = [[-1.3, -1.2], [-1.5, -5]]  # Coefficients of the inequality constraints
    b = [-5, -10]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraint)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = res.fun  # Optimal cost value

    return obj