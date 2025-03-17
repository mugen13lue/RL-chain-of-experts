from scipy.optimize import linprog

def prob_76(light_grilled_cheese_sandwiches, heavy_grilled_cheese_sandwiches):
    c = [10, 15]  # Coefficients of the objective function to minimize total production time

    A = [
        [2, 3],  # Coefficients of bread constraint
        [3, 5],  # Coefficients of cheese constraint
        [-3, 1]  # Coefficients of at least 3 times as many heavy sandwiches as light sandwiches constraint
    ]

    b = [300, 500, 0]  # RHS values of the constraints

    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    total_production_time = res.fun  # Total production time is the optimal value of the objective function

    return total_production_time