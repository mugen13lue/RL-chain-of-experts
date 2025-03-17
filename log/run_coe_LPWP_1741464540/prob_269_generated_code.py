from scipy.optimize import linprog

def prob_269():
    c = [-3, -10]  # Coefficients of the objective function to maximize (3x + 10y)
    A = [[3, 0], [0, 10], [-1, -1], [0, -1]]  # Coefficients of the inequality constraints
    b = [200, 200, -4, 0.33]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    return int(res.fun)  # Return the optimal value of the objective function