from scipy.optimize import linprog

def prob_260(method_A, method_B, required_fabric, required_plastic, available_special_element):
    """
    Solve the problem to minimize the total time needed.

    Args:
        method_A: an integer representing the number of executions of Method A
        method_B: an integer representing the number of executions of Method B
        required_fabric: an integer representing the minimum required units of fabric
        required_plastic: an integer representing the minimum required units of plastic
        available_special_element: an integer representing the available units of the special element

    Returns:
        objective_value: an integer representing the minimized total time needed
    """
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    A = [[-25, -45], [-14, -25], [60, 65]]  # Coefficients of the constraints
    b = [-required_fabric, -required_plastic, available_special_element]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    objective_value = res.fun  # Minimized total time needed

    return objective_value