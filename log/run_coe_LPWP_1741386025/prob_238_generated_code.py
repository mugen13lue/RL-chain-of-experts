from scipy.optimize import linprog

def prob_238(large_pizzas, medium_pizzas):
    c = [8, 12]  # Coefficients of the objective function (baking time)
    A = [[8, 12], [4, 5], [0, 1], [-2, 1]]  # Coefficients of the constraints
    b = [10000, 4400, 200, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    if res.success:
        return res.fun
    else:
        return "Optimization failed"