from scipy.optimize import linprog

def prob_193(car, bus, constraint1, constraint2):
    c = [10, 30]  # Coefficients of the objective function to minimize 10x + 30y
    A = [[4, 20], [0, 1]]  # Coefficients of the constraints
    b = [constraint1, constraint2]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, 4)])

    return int(res.fun)  # Return the minimized total pollution produced