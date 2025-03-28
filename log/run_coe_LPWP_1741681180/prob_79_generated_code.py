from scipy.optimize import linprog

def prob_79(peanut_butter_crepes, chocolate_crepes):
    c = [6, 7]  # Coefficients of the objective function (crepe mix)
    A = [[3, 4], [6, 7], [-1, 1], [-0.75, -0.75]]  # Coefficients of the inequality constraints
    b = [400, 450, 0, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Return the total amount of crepe mix needed