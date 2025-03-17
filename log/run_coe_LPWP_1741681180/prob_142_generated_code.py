from scipy.optimize import linprog

def prob_142():
    c = [-5, -6]  # Coefficients of the objective function to maximize (-5x - 6y)
    A = [[3, 5], [4, 3], [1, 2]]  # Coefficients of the left-hand side of the constraints
    b = [80, 70, 10]  # Right-hand side of the constraints
    x_bounds = (0, None)  # Bounds for x (experiment 1)
    y_bounds = (0, None)  # Bounds for y (experiment 2)

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    return res.fun * -1  # Return the negative of the optimal objective value to maximize

# Call the function and print the result
print(prob_142())