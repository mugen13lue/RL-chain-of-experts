from scipy.optimize import linprog

def prob_93(generator_A, generator_B):
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-40, -30], [300, 200]]  # Coefficients for the inequality constraints
    b = [-1000, 3000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun