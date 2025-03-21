from scipy.optimize import linprog

def prob_187(ferry, light_rail, constraint1, constraint2, constraint3):
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-20, -15], [0, -1], [-4, 1]]  # Coefficients for the constraints
    b = [-500, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    return res.fun