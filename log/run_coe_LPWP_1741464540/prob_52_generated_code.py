from scipy.optimize import linprog

def prob_52(dine_in_place, food_truck):
    """
    Args:
        dine_in_place: an integer, representing the number of dine-in places
        food_truck: an integer, representing the number of food trucks
    Returns:
        obj: an integer, representing the objective value (total number of stores)
    """
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    A = [[-100, -50], [8, 3]]  # Coefficients of the production and employee constraints
    b = [-500, 35]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res.fun