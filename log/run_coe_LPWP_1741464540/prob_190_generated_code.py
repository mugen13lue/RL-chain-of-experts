from scipy.optimize import linprog

def prob_190(small_crates, large_crates):
    c = [-200, -500]  # Coefficients of the objective function to maximize (200x + 500y)
    A = [[1, 0], [0, 1], [-1, -3], [1, 1], [0, -1]]  # Coefficients of the constraints
    b = [small_crates, large_crates, 0, 60, -10]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    total_grapes = -res.fun  # Maximum total number of grapes transported

    return total_grapes