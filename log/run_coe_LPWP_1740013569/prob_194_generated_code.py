from scipy.optimize import linprog

def prob_194(small_trucks, large_trucks):
    c = [-30, -50]  # Coefficients of the objective function to maximize 30x + 50y

    A = [[2, 4], [-1, 0], [0, -1], [-2, 1]]  # Coefficients of the inequality constraints
    b = [30, -10, -3, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b)  # Using linear programming to maximize the objective function

    return int(-res.fun)  # Returning the maximum amount of snow that can be transported