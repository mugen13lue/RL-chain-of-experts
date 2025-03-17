from scipy.optimize import linprog
import numpy as np

def prob_232(circular_tables, rectangular_tables):
    c = [-8, -12]  # Coefficients of the objective function to maximize 8x + 12y

    A = np.array([
        [4, 4],
        [4, 5],
        [15, 20]
    ])  # Coefficients of the constraints

    b = np.array([500, 300, 1900])  # Right-hand side of the constraints

    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraint)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs', options={"integer_tol": 1e-5})

    return int(-res.fun)  # Return the maximum number of catered guests