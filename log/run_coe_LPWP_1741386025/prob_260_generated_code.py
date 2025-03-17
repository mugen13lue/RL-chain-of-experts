from scipy.optimize import linprog

def prob_260(method_A, method_B, required_fabric, required_plastic, available_special_element):
    c = [1, 1]  # Coefficients for the objective function to minimize total time
    A = [[-25, -45], [-14, -25], [60, 65]]  # Coefficients for the constraints
    b = [-required_fabric, -required_plastic, available_special_element]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun