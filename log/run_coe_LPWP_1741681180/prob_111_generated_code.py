from scipy.optimize import linprog

def prob_111(x, y, constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    c = [4, 6]  # coefficients for unsaturated fat intake in crab cakes and lobster rolls
    A = [[-5, -8], [-7, -4], [1, -0.4], [1, -0.4], [-1, 0], [0, -1]]  # coefficients for vitamin A and C constraints
    b = [-constraint1, -constraint2, 0, 0, constraint5, constraint6]  # right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b)  # solving the linear programming problem

    return res.fun