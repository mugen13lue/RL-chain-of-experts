from scipy.optimize import linprog

def prob_114(apple_flavored_baby, carrot_flavored_baby):
    c = [-2, -4]  # Coefficients of the objective function to maximize 2x + 4y
    A = [[2, 4], [5, 3], [-1, 3], [0, -1]]  # Coefficients of the constraints
    b = [apple_flavored_baby, carrot_flavored_baby, 0, -2]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    objective_value = -res.fun  # Maximum fat intake

    return objective_value