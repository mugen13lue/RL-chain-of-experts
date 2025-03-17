from scipy.optimize import linprog

def prob_225(wide_pipes, narrow_pipes):
    c = [1, 1]  # Coefficients for the objective function Z = x + y
    A = [[-25, -15], [-1, 0], [0, -1], [1, 0]]  # Coefficients for the constraints
    b = [-900, -5, 0, -5]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(wide_pipes, None), method='highs')
    return int(res.fun)  # Minimum total number of pipes required