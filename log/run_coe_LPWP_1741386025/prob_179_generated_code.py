from scipy.optimize import linprog

def prob_179(cargo_planes, ultrawide_trucks):
    """
    Args:
        cargo_planes: an integer, number of cargo planes
        ultrawide_trucks: an integer, number of ultrawide trucks
    Returns:
        obj: an integer, minimum number of trips
    """
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    A = [[10, 6], [1000, 700], [-1, 1]]  # Coefficients of the constraints
    b = [200, 22000, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Minimum number of trips