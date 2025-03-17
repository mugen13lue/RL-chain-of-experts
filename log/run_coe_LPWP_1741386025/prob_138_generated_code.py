from scipy.optimize import linprog

def prob_138(medicine_A, medicine_B):
    c = [-12, -8]  # Coefficients of the objective function to be minimized (-12x - 8y)
    A = [[30, 40], [50, 30], [-1, 0], [0, -1]]  # Coefficients of the left-hand side of constraints
    b = [300, 400, -5, 0]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum number of people that can be treated