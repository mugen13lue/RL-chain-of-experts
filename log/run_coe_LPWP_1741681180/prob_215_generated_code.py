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
    c = [-250, -375]  # We want to maximize earnings, so we use negative values

    # Coefficients of the inequality constraints
    A = [[30, 20], [90, 125]]  # Inspection time and fixing time constraints
    b = [constraint1, constraint2]  # Available minutes constraints

    # Bounds for the variables
    x_bounds = (0, None)  # Non-negativity constraint for washing machines
    y_bounds = (0, None)  # Non-negativity constraint for freezers

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    obj = -res.fun  # Maximized earnings

    return obj