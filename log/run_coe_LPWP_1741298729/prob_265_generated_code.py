from scipy.optimize import linprog

def prob_265():
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y

    A = [
        [-1, -1],  # Coefficients of Constraint 1: x + y >= 80
        [-0.6, -1],  # Coefficients of Constraint 2: x <= 0.6(x + y)
        [1, 0],     # Coefficients of Constraint 3: x >= 0
        [0, 1]      # Coefficients of Constraint 4: y >= 0
    ]

    b = [-80, 0, 0, 0]  # Right-hand side values of the constraints

    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negative)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun

# Call the function to get the objective value
obj = prob_265()
print(obj)