from scipy.optimize import linprog

def prob_38(A, B):
    c = [4, 12]  # Coefficients of the objective function to minimize K
    A_ub = [[-8, -15], [-6, -2], [10, 20]]  # Coefficients for the constraints
    b_ub = [-150, -300, 400]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, None))

    return res.fun