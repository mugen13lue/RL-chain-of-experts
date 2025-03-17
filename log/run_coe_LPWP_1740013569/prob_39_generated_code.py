from scipy.optimize import linprog

def prob_39(chocolate_ice_cream, vanilla_ice_cream):
    c = [-200, -300]  # Coefficients of the objective function to minimize (-200x - 300y)
    A = [[-1, 0], [0, -1], [1, 0], [0, 1], [1, 2], [-1, 0], [0, -2]]  # Coefficients of the constraints
    b = [-5, -5, 10, 8, 30, -6, -2]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(5, 10), (5, 8)], method='highs')

    return -res.fun  # Return the maximum profit