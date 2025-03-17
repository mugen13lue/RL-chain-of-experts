from scipy.optimize import linprog

def prob_243(original_meal, experimental_meal):
    c = [10, 15]  # Coefficients of the objective function to minimize cooking time
    A = [[20, 25], [45, 35]]  # Coefficients of the constraints
    b = [800, 900]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    if res.success:
        obj = res.fun  # Minimized cooking time
        return obj
    else:
        return "Optimization failed"