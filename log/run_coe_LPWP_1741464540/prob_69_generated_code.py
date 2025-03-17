from scipy.optimize import linprog

def prob_69(brownies, lemon_squares):
    """
    Args:
        brownies: an integer, the number of brownies to be made
        lemon_squares: an integer, the number of lemon squares to be made
        
    Returns:
        obj: an integer, the total amount of fiber needed
    """
    c = [4, 6]  # Coefficients of the objective function (fiber)
    A = [[5, 7], [4, 6], [-1, 1], [-0.6, -0.6]]  # Coefficients of the inequality constraints
    b = [2500, 3300, 0, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Total amount of fiber needed