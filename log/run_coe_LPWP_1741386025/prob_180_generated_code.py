from scipy.optimize import linprog

def prob_180():
    c = [-40, -100]  # Coefficients of the objective function to be minimized
    A = [[1, 1], [0, 1], [1, 0], [-2, 1]]  # Coefficients of the left-hand side of constraints
    b = [25, 10, 30, 0]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, 30), (5, 10)], method='highs')

    return int(-res.fun)  # Return the maximum amount of glacial water that can be transported