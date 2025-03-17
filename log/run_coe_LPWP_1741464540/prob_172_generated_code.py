from scipy.optimize import linprog

def prob_172(bus, car):
    """
    Args:
        bus: an integer
        car: an integer
    Returns:
        obj: an integer
    """
    # Coefficients of the objective function
    c = [2, 1.5]

    # Coefficients of the constraints
    A = [[100, 40], [-1, -1]]
    b = [1200, 0]
    bounds = [(0, bus), (0, None)]

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    obj = round(res.fun, 2)
    
    return obj