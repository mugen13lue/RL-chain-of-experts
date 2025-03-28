from scipy.optimize import linprog

def prob_208(health_supplement_A, health_supplement_B):
    c = [14, 25]  # Coefficients of the objective function to minimize cost
    A = [[-30, -60], [-50, -10]]  # Coefficients of the inequality constraints
    b = [-400, -50]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun