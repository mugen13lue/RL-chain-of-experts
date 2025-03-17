from scipy.optimize import linprog

def prob_216():
    c = [12, 10, 15]  # Coefficients of the objective function to maximize (12x1 + 10x2 + 15x3)
    A = [[400, 500, 450], [200, 300, 350]]  # Coefficients of the inequality constraints
    b = [20000, 14000]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None), (0, None)]  # Bounds for the decision variables x1, x2, x3

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    return res.fun  # Return the maximum profit

# Call the function to get the maximum profit
max_profit = prob_216()
print("Maximum profit: $", max_profit)