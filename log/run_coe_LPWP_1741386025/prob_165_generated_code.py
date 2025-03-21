from scipy.optimize import linprog

def prob_165(electric_bikes, scooters, Max_Bikes, Min_Scooters, Charge_Limit):
    """
    Args:
        electric_bikes: an integer, the number of electric bikes used.
        scooters: an integer, the number of scooters used.
        Max_Bikes: an integer, maximum number of electric bikes allowed.
        Min_Scooters: an integer, minimum number of scooters required.
        Charge_Limit: an integer, available charge units.

    Returns:
        Number_of_Meals: an integer, the maximum number of meals that can be delivered.
    """
    c = [-8, -5]  # Coefficients of the objective function to be minimized
    A = [[3, 2], [-1, 0.3], [0, -1]]  # Coefficients of the inequality constraints
    b = [Charge_Limit, 0, -Min_Scooters]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, Max_Bikes), (0, None)])

    return int(-res.fun)  # Return the maximum number of meals that can be delivered