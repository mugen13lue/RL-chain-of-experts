def prob_164():
    """
    Solve the sand delivery problem and maximize the amount of sand that can be delivered.

    Returns:
        objective_value: the amount of sand that can be delivered (objective value of the problem)
    """
    from scipy.optimize import linprog

    # Coefficients of the objective function
    c = [-20, -50]  # Maximizing 20x + 50y is equivalent to minimizing -20x - 50y

    # Coefficients of the inequality constraints
    A = [[1, 0], [0, 1], [-1, 3], [1, -3]]
    b = [5, 3, 0, 0]

    # Bounds for variables x and y
    x_bounds = (5, None)
    y_bounds = (3, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    objective_value = -res.fun  # Convert the minimized value back to maximized value

    return objective_value

# Call the function to get the maximum amount of sand that can be delivered
result = prob_164()
print(result)