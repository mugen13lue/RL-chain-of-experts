from scipy.optimize import linprog

def prob_239():
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y

    A = [
        [-1, -1],  # Coefficients of the inequality constraint x + y >= 400
        [-0.7, 0]  # Coefficients of the inequality constraint x >= 0.7(x + y)
    ]

    b = [-400, 0]  # Right-hand side of the inequality constraints

    bounds = [(0, None), (0, None)]  # Bounds for variables x and y (non-negative)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res

# Call the function and print the result
result = prob_239()
print(result)