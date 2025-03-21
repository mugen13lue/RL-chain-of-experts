from scipy.optimize import linprog

def prob_165(Max_Bikes, Min_Scooters, Charge_Limit):
    c = [8, 5]  # Coefficients of the objective function to maximize (8x + 5y)
    A = [[3, 2], [-1, -0.3], [0, -1]]  # Coefficients of the inequality constraints
    b = [Charge_Limit, 0, -Min_Scooters]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Return the maximum number of meals that can be delivered