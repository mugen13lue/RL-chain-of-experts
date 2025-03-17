from scipy.optimize import linprog

def prob_176(small, large):
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[50, 200]]  # Coefficients for the constraint 50x + 200y >= 100000
    b = [100000]  # Right-hand side of the constraint

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Return the minimum number of jars