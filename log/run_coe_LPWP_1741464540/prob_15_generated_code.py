from scipy.optimize import linprog

def prob_15(senior_citizens, young_adults):
    c = [500, 750]  # Coefficients of the objective function (wage bill)
    A = [[500, 750], [1, 1], [0, 1], [-1/3, 1]]  # Coefficients of the constraints
    b = [30000, 50, 10, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Return the minimized wage bill