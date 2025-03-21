from scipy.optimize import linprog

def prob_246(LED_fixture, fluorescence_lamp):
    """
    Args:
        LED_fixture: an integer, the number of LED fixtures to be installed
        fluorescence_lamp: an integer, the number of fluorescence lamps to be installed

    Returns:
        obj: an integer, the total number of light changes
    """
    c = [3, 4]  # Coefficients of the objective function to minimize 3L + 4F
    A = [[5, 8], [-1, -1]]  # Coefficients of the inequality constraints
    b = [2000, -300]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables L and F

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = res.fun  # Total number of light changes

    return obj