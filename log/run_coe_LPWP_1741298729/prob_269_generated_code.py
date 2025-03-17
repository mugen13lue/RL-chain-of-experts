from scipy.optimize import linprog

def prob_269():
    c = [-3, -10]  # Coefficients of the objective function to maximize 3x + 10y

    A = [[3, 10], [1, -3]]  # Coefficients of the inequality constraints
    b = [200, 0]  # Right-hand side of the inequality constraints

    bounds = [(4, None), (0, None)]  # Bounds for x (number of runners) and y (number of canoers)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun * -1  # The optimal value of the objective function (maximized)

# Call the function to get the result
result = prob_269()
print(result)