from scipy.optimize import linprog

def prob_166(large_planes, small_planes):
    c = [1, 1]  # Coefficients of the objective function to minimize x + y
    A = [[30, 10], [-1, 1]]  # Coefficients of the constraints
    b = [300, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    return int(res.fun)  # Return the minimum number of planes used