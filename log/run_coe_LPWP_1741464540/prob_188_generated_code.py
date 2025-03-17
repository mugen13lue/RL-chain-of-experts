from scipy.optimize import linprog

def prob_188():
    c = [1, 0]  # Coefficients for the objective function to minimize x
    A = [[1, 1], [0, 1], [-0.6, -0.6]]  # Coefficients for the constraints
    b = [500, 30, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.x[0])  # Return the minimized total number of taxi rides