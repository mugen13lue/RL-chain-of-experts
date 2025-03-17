from scipy.optimize import linprog

def prob_98(vintage_bottles, regular_bottles):
    c = [-1, -1]  # Coefficients for the objective function to maximize x + y
    A = [[500, 750], [-4, 1], [1, 0]]  # Coefficients for the constraints
    b = [100000, 0, 10]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum total number of bottles produced