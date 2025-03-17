from scipy.optimize import linprog

def prob_122(cheap_box, expensive_box, constraint1, constraint2, constraint3):
    c = [-8, -10]  # Coefficients of the objective function to minimize (-8x - 10y)
    A = [[3, 5], [5, 8], [2, 3]]  # Coefficients of the constraints
    b = [constraint1[2], constraint2[2], constraint3[2]]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum amount of foam produced