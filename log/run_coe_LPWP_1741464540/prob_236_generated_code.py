from scipy.optimize import linprog

def prob_236(bikes, scooters):
    """
    Solves the transportation problem to maximize tips received.

    Args:
        bikes: an integer representing the number of shifts on bikes
        scooters: an integer representing the number of shifts on scooters

    Returns:
        obj: an integer representing the maximum tips received
    """
    c = [-50, -43]  # Coefficients of the objective function to minimize (-50x - 43y)
    A = [[1, 1], [5, 6], [-10, -7], [0, -1]]  # Coefficients of the constraints
    b = [40, 230, -320, -5]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(5, None), (5, None)], method='highs')
    obj = -res.fun  # Maximum tips received

    return obj