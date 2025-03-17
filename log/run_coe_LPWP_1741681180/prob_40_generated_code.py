from scipy.optimize import linprog

def prob_40():
    # Coefficients of the objective function (profit per acre)
    c = [-500, -650]  # Negative values for maximization

    # Coefficients of the inequality constraints
    A = [[-1, 0], [0, -1], [-2, 1], [1, 1]]
    b = [-12, -15, 0, 50]

    # Bounds for variables x and y
    x_bounds = (12, None)  # x >= 12
    y_bounds = (15, None)  # y >= 15

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values and profit
    optimal_potatoes = res.x[0]
    optimal_cucumbers = res.x[1]
    max_profit = -res.fun  # Convert back to positive value

    return optimal_potatoes, optimal_cucumbers, max_profit

# Call the function and print the results
optimal_potatoes, optimal_cucumbers, max_profit = prob_40()
print(f"Optimal acres of potatoes: {optimal_potatoes}")
print(f"Optimal acres of cucumbers: {optimal_cucumbers}")
print(f"Maximum profit: ${max_profit}")