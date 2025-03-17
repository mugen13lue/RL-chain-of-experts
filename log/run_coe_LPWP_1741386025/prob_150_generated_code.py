from scipy.optimize import linprog

def prob_150(small_bottles, large_bottles):
    c = [-5, -20]  # Coefficients of the objective function to maximize (5x + 20y)
    A = [[5, 20], [1, 0], [0, 1], [-1, -2], [0, -1], [1, 1]]  # Coefficients of the left-hand side of constraints
    b = [200, 300, 100, 0, -50, 200]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b)
    max_honey = res.fun  # Maximum amount of honey that can be transported

    return int(-max_honey)