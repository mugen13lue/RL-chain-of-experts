from scipy.optimize import linprog

def prob_272(medication_patches, anti_biotic_creams):
    c = [-3, -2]  # Coefficients of the objective function to maximize 3x + 2y

    A = [[3, 5], [5, 6], [1, 1], [0, -2]]  # Coefficients of the constraints
    b = [400, 530, 100, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum number of people that can be treated