from scipy.optimize import linprog

def prob_232(circular_tables, rectangular_tables):
    c = [-8, -12]  # Coefficients of the objective function to maximize 8x + 12y

    A = [
        [4, 4],
        [4, 5],
        [15, 20]
    ]  # Coefficients of the constraints

    b = [500, 300, 1900]  # Right-hand side of the constraints

    bounds = [(0, None), (0, None)]  # Non-negativity constraints for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum number of catered guests