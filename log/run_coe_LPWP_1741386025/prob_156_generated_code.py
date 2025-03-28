from scipy.optimize import linprog

def prob_156(vans, trucks):
    c = [1]  # Coefficients of the objective function (minimize x)
    A = [[50, 100]]  # Coefficients of the left-hand side of the inequality constraints
    b = [2000]  # Right-hand side of the inequality constraints
    bounds = [(0, None)]  # Bounds for the variables (x >= 0)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    return int(res.x[0])