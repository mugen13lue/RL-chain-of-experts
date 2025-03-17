from scipy.optimize import linprog

def prob_178(bike, car):
    """
    Args:
        bike: an integer, represents the number of bikes
        car: an integer, represents the number of cars
    Returns:
        obj: an integer, the objective value
    """
    
    c = [0, 1]  # Coefficients for the objective function (minimize y)
    
    A = [
        [-1, -1],  # x + y >= 100
        [-5, -3],  # 5x + 3y >= 500
        [-0.6, 0.4]  # x <= 0.4(x + y)
    ]
    
    b = [-100, -500, 0]  # RHS of the constraints
    
    bounds = [(0, None), (0, None)]  # Bounds for x and y
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    obj = res.fun  # Objective value (total number of bikes needed)
    
    return int(obj)