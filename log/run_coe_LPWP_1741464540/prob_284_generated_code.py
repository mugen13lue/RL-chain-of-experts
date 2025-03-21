from scipy.optimize import linprog

def prob_284(heavy_duty_yard_machine, gas_lawn_mower):
    """
    Args:
        heavy_duty_yard_machine: an integer, the maximum square feet to be cut using heavy duty yard machine
        gas_lawn_mower: an integer, the maximum square feet to be cut using gas lawn mower

    Returns:
        obj: an integer, the objective value (time required)
    """
    # Coefficients of the objective function
    c = [2, 5]

    # Coefficients of the inequality constraints
    A = [[2, 5], [3, 2], [12, 10]]
    b = [2500, 450, 2000]

    # Bounds for the variables x and y based on input arguments
    x_bounds = (0, heavy_duty_yard_machine)
    y_bounds = (0, gas_lawn_mower)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    # Calculate the objective value (time required)
    obj = c[0]*x_opt + c[1]*y_opt

    return obj