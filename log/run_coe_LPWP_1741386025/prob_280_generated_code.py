from scipy.optimize import linprog

def prob_280(bus, personal_car):
    """
    Args:
        bus: an integer, represents the number of buses
        personal_car: an integer, represents the number of personal cars
    Returns:
        obj: an integer, the total number of vehicles
    """
    c = [1, 1]  # Coefficients for the objective function to minimize Z = x + y
    A = [[9, 4], [-1, 0]]  # Coefficients for the constraints
    b = [100, -5]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    obj = res.fun  # Total number of vehicles

    return int(obj)