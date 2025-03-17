from scipy.optimize import linprog

def prob_221():
    c = [-450, -1200]  # Coefficients of the objective function to minimize (-450x - 1200y)
    A = [[1, 1], [550, 2000]]  # Coefficients of the inequality constraints
    b = [300, 400000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

    x = int(res.x[0])  # Number of personal licenses produced
    y = int(res.x[1])  # Number of commercial licenses produced
    objective_value = -int(res.fun)  # Maximum profit

    return x, y, objective_value