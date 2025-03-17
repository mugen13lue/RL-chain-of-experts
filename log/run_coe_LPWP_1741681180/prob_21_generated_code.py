from scipy.optimize import linprog

def prob_21(bread, cookies):
    c = [-5, -3]  # Coefficients of the objective function to minimize (-5x - 3y)
    A = [[1, 0.5], [3, 1]]  # Coefficients of the inequality constraints
    b = [3000, 3000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return -res.fun  # Return the maximum total profit