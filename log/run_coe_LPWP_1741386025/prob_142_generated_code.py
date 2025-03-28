from scipy.optimize import linprog

def prob_142(experiment_1, experiment_2, constraint_1, constraint_2, constraint_3, constraint_4, constraint_5, constraint_6, constraint_7, constraint_8):
    """
    Args:
        experiment_1: an integer, number of experiments of type 1
        experiment_2: an integer, number of experiments of type 2
        constraint_1: an integer, constraint on the availability of red liquid for experiment 1
        constraint_2: an integer, constraint on the availability of blue liquid for experiment 1
        constraint_3: an integer, constraint on the availability of red liquid for experiment 2
        constraint_4: an integer, constraint on the availability of blue liquid for experiment 2
        constraint_5: an integer, constraint on the production of smelly gas for experiment 1
        constraint_6: an integer, constraint on the production of smelly gas for experiment 2
        constraint_7: an integer, constraint on the maximum total production of smelly gas
        constraint_8: an integer, constraint on the maximum total production of green gas

    Returns:
        obj: an integer, the objective value (total amount of green gas produced)
    """
    c = [-5, -6]  # Coefficients of x and y in the objective function Z = 5x + 6y
    A = [[3, 5], [4, 3], [1, 2]]  # Coefficients of x and y in the constraints
    b = [constraint_1, constraint_2, constraint_5]  # Right-hand side of the constraints
    x_bounds = (0, None)
    y_bounds = (0, None)

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    x_opt = res.x[0]
    y_opt = res.x[1]

    total_green_gas = -res.fun

    return total_green_gas