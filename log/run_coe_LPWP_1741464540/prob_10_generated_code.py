from scipy.optimize import linprog

def prob_10(A, B, constraint1, constraint2, constraint3):
    c = [0, 0, -1]  # Coefficients for the objective function to minimize D
    A_eq = [[5, 9, -1]]  # Coefficients for the equality constraint 5x + 9y = D
    b_eq = [0]  # Right-hand side of the equality constraint

    A_ub = [[-13, -8, 0], [-5, -14, 0], [6, 6, 0]]  # Coefficients for the inequality constraints
    b_ub = [-constraint1, -constraint2, -constraint3]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(0, None))

    return int(res.x[0]), int(res.x[1]), int(res.fun * -1)