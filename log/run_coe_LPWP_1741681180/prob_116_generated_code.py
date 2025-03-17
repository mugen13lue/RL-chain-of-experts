from scipy.optimize import linprog

def prob_116(acne_cream_rate, anti_bacterial_cream_rate, base_gel):
    c = [1, 1]  # Coefficients for the objective function to minimize total time
    A = [[-acne_cream_rate, -anti_bacterial_cream_rate], [-15, -10]]  # Coefficients for the inequality constraints
    b = [-800, -1000]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    total_time = res.fun  # Total time needed to minimize the total time

    return total_time