from scipy.optimize import linprog

def prob_149(vans, trucks):
    """
    Args:
        vans: an integer, the number of trips by vans
        trucks: an integer, the number of trips by trucks
    Returns:
        obj: an integer, the objective value
    """
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-50, -80], [30, 50], [-1, 1]]  # Coefficients for the constraints
    b = [-1500, 1000, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

    return res.fun