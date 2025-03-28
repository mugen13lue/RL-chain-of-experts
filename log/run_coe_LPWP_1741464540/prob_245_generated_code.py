from scipy.optimize import linprog

def prob_245():
    c = [20, 15]  # Coefficients of the objective function to minimize 20x + 15y
    A = [[-1, 0], [0, -1], [-1, -1], [-2000, -800]]  # Coefficients of the inequality constraints
    b = [-7, 0, 0, -20000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, 7), (0, None)])  # Solve the linear programming problem

    amount_of_pollution = res.fun  # Total amount of pollution produced

    return amount_of_pollution

# Call the function to get the result
print(prob_245())