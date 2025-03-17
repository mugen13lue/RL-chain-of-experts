from scipy.optimize import linprog

def prob_79(peanut_butter_crepes, chocolate_crepes):
    c = [6, 7]  # Coefficients of the objective function to minimize 6x + 7y
    A = [[-3, 0], [0, -4], [-6, -7], [-0.75, -0.75], [-1, 1]]  # Coefficients of the constraints
    b = [-400, -450, 0, 0, 1]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun