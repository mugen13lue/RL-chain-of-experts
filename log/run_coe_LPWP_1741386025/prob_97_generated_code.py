def prob_97(premium_model, regular_model):
    """
    Args:
        premium_model: an integer, number of premium printers
        regular_model: an integer, number of regular printers
    Returns:
        objective_value: an integer, total number of printers
    """
    from scipy.optimize import linprog

    c = [1, 1]  # Coefficients of the objective function to minimize x + y

    A = [[-30, -20],  # Pages per minute constraint: 30x + 20y >= 200
         [4, 3],      # Ink per minute constraint: 4x + 3y <= 35
         [0, 1]]      # Number of regular printers constraint: y <= x

    b = [-200, 35, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.x[0]), int(res.x[1])  # Return the optimal number of premium and regular printers