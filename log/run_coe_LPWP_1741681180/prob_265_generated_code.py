from scipy.optimize import linprog

def prob_265():
    """
    Returns:
        obj: an integer, the objective value
    """
    # Coefficients of the objective function
    c = [1, 1]  # minimize the total number of carts

    # Coefficients of the inequality constraints
    A = [[4, 1]]  # golf carts can take 4 guests, pull carts can take 1 guest
    b = [80]  # need to transport at least 80 guests

    # Coefficients of the equality constraints
    A_eq = [[-0.6, -0.4]]  # at most 60% of carts can be golf carts
    b_eq = [0]

    # Bounds for the variables
    x_bounds = (0, None)  # number of golf carts
    y_bounds = (0, None)  # number of pull carts

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=[x_bounds, y_bounds])

    obj = res.fun  # the objective value

    return obj

# Call the function to get the objective value
result = prob_265()
print(result)