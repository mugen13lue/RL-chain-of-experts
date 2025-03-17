from scipy.optimize import linprog

def prob_175(seasonal, full_time):
    c = [-5, -8]  # Coefficients of the objective function to maximize gifts delivered
    A = [[5, 8], [2, 5], [-1, 0.3], [0, -0.9]]  # Coefficients of the constraints
    b = [0, 200, 0, -10]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum total number of gifts that can be delivered