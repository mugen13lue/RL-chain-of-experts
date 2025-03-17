from scipy.optimize import linprog

def prob_61():
    c = [1, 1]  # Coefficients of the objective function to minimize x + y
    A = [[-1, 0], [0, -1], [-10, -15], [200, 250]]  # Coefficients of the inequality constraints
    b = [-5, 0, -200, 3500]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(5, None))  # Solving the linear program

    return res.fun  # Return the optimal objective value