from scipy.optimize import linprog

def prob_246(LED_fixture, fluorescence_lamp):
    """
    Args:
        LED_fixture: an integer, the number of LED fixtures to be installed
        fluorescence_lamp: an integer, the number of fluorescence lamps to be installed

    Returns:
        obj: an integer, the total number of light changes
    """
    obj = 3 * LED_fixture + 4 * fluorescence_lamp

    # Define the coefficients of the objective function
    c = [3, 4]

    # Define the coefficients of the inequality constraints
    A = [[5, 8], [-1, -0.3], [-1, -1]]
    b = [2000, 0, -300]

    # Define the bounds for the variables
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    return res.fun