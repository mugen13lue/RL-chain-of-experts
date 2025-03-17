from scipy.optimize import linprog

def prob_245():
    c = [20, 15]  # Coefficients of the objective function to minimize
    A = [[2000, 800], [-1, -1], [0, -0.6]]  # Coefficients of the inequality constraints
    b = [20000, -7, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    amount_of_pollution = res.fun  # Total amount of pollution produced

    return amount_of_pollution