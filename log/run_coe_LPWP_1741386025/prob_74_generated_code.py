from scipy.optimize import linprog

def prob_74(with_a_catalyst, without_a_catalyst):
    """
    Args:
        with_a_catalyst: an integer (number of process with a catalyst),
        without_a_catalyst: an integer (number of process without a catalyst),

    Returns:
        obj: an integer (amount of carbon dioxide produced),
    """
    # Coefficients of the objective function
    c = [-15, -18]  # Coefficients are negated for maximization

    # Coefficients of the inequality constraints
    A = [[10, 15], [20, 12]]  # Coefficients of wood and oxygen constraints
    b = [300, 300]  # Available units of wood and oxygen

    # Bounds for variables (x, y >= 0)
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solving the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extracting the optimal values
    x_opt = res.x[0]
    y_opt = res.x[1]
    obj_val = -res.fun  # Objective value is negated back to positive

    return round(obj_val)