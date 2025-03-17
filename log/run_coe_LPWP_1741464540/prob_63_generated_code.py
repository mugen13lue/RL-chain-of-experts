from scipy.optimize import linprog

def prob_63():
    c = [1, 1]  # Coefficients of the objective function to minimize z = x + y
    A = [[-80, -150], [50, 70]]  # Coefficients of the inequality constraints
    b = [-1000, 500]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the decision variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res.fun