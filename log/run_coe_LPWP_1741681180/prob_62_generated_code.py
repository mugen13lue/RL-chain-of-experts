from scipy.optimize import linprog

def prob_62(rural, urban, _100, _8, _200, _20, _260, _3000):
    """
    Args:
        rural: an integer, number of rural factories
        urban: an integer, number of urban factories
        _100: an integer, number of phones that a rural factory can make per day
        _8: an integer, number of managers required for a rural factory
        _200: an integer, number of phones that an urban factory can make per day
        _20: an integer, number of managers required for an urban factory
        _260: an integer, available number of managers
        _3000: an integer, minimum number of phones required per day
    Returns:
        number_of_factories: an integer, total number of factories
    """
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    A = [[-8, -20], [100, 200]]  # Coefficients of the inequality constraints
    b = [-260, 3000]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Non-negativity constraints for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res.x[0], res.x[1]