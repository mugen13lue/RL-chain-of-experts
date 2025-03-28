from scipy.optimize import linprog

def prob_104(orange_juice, apple_juice):
    c = [-10, -12]  # Coefficients of the objective function to maximize (negative because linprog minimizes)
    A = [[10, 12], [8, 6]]  # Coefficients of the constraints
    b = [orange_juice, apple_juice]  # Right-hand side of the constraints
    bounds = [(3, None), (3*orange_juice, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum total vitamin D intake