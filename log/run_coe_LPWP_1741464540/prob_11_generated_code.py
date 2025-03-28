from scipy.optimize import linprog

def prob_11():
    c = [-0.50, -1]  # Coefficients of the objective function to maximize profit
    A = [[1, 1], [-0.8, 1], [0, -1]]  # Coefficients of the inequality constraints
    b = [760000, 0, -20000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (20000, None)])
    
    return -res.fun  # Maximum profit is the negative of the minimum value returned by linprog