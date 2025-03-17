from scipy.optimize import linprog

def prob_6():
    c = [-350, -600]  # Coefficients of the objective function to minimize (-1 * profit)
    A = [[1, 1], [1, 0], [0, 1], [-2, 1]]  # Coefficients of the inequality constraints
    b = [140, 20, 30, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    max_profit = -res.fun  # Convert the minimized profit back to maximized profit

    return int(max_profit)