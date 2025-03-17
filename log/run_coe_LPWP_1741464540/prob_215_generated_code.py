from scipy.optimize import linprog

def prob_215(freezers, washing_machine, constraint1, constraint2):
    """
    Args:
        freezers: an integer representing the number of freezers
        washing_machine: an integer representing the number of washing machines
        constraint1: an integer representing the first constraint
        constraint2: an integer representing the second constraint
    Returns:
        obj: an integer representing the objective value
    """
    # Coefficients of the objective function
    c = [-250, -375]  # We are maximizing earnings, so we use negative values

    # Coefficients of the inequality constraints
    A = [[30, 20], [90, 125]]
    b = [constraint1, constraint2]

    # Bounds for the variables
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    washing_machines_fixed = round(res.x[0])
    freezers_fixed = round(res.x[1])

    # Calculate the maximum earnings
    max_earnings = -res.fun

    print(f"Number of washing machines to fix: {washing_machines_fixed}")
    print(f"Number of freezers to fix: {freezers_fixed}")
    print(f"Maximum earnings: ${max_earnings}")

    return max_earnings