from scipy.optimize import linprog

def prob_205(protein_bars, noodles):
    c = [5, 2.5]  # Cost coefficients
    A = [[600, 250], [1.5, 5]]  # Coefficients for calorie and protein constraints
    b = [2000, 16]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun