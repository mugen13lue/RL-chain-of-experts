from scipy.optimize import linprog

def prob_48(factory_1, factory_2, constraint_1, constraint_2, constraint_3):
    c = [300, 600]  # Coefficients of the objective function (cost)
    A = [[5, 10], [6, 10], [3, 0]]  # Coefficients of the inequality constraints
    b = [constraint_1, constraint_2, constraint_3]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    cost = res.fun  # Minimized cost of production

    return cost