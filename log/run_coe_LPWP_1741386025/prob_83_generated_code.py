from scipy.optimize import linprog

def prob_83(var_4wheeler, var_3wheeler):
    """
    Args:
        var_4wheeler: an integer, number of 4-wheeler vehicles
        var_3wheeler: an integer, number of 3-wheeler vehicles
    Returns:
        obj: an integer, objective value
    """
    c = [1, 1]
    A = [[-60, -40], [30, 15]]
    b = [-1000, 430]
    x_bounds = (0, None)
    y_bounds = (0, None)

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    optimal_x = var_4wheeler
    optimal_y = var_3wheeler

    obj = optimal_x + optimal_y

    return round(obj)