from scipy.optimize import linprog

def prob_170(small_suitcases, large_suitcases):
    c = [-50, -80]  # Coefficients of the objective function to maximize -50x - 80y
    A = [[1, 0], [-2, -1], [1, 0], [0, 1], [0, -1]]  # Coefficients of the inequality constraints
    b = [70, -15, 70, 50, -50]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, small_suitcases), (15, large_suitcases)], method='highs')

    return int(-res.fun)  # Return the maximum number of snacks that can be delivered