from scipy.optimize import linprog

def prob_71(top_loading_model, front_loading_model, items_top_loading, items_front_loading, energy_top_loading, energy_front_loading):
    """
    Args:
        top_loading_model: an integer, representing the number of top-loading machines
        front_loading_model: an integer, representing the number of front-loading machines
        items_top_loading: an integer, representing the number of items the top-loading model can wash per day
        items_front_loading: an integer, representing the number of items the front-loading model can wash per day
        energy_top_loading: an integer, representing the amount of energy consumed by the top-loading model per day
        energy_front_loading: an integer, representing the amount of energy consumed by the front-loading model per day
    Returns:
        obj: an integer, representing the minimum total number of washing machines
    """
    
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    
    A = [
        [-items_top_loading, -items_front_loading],  # Items Constraint: 50x + 75y >= 5000
        [energy_top_loading, energy_front_loading],    # Energy Constraint: 85x + 100y <= 7000
        [-1, -1],        # Top-loading Limit: x <= 0.4(x+y)
        [0, 1]           # Front-loading Minimum: y >= 10
    ]
    
    b = [-5000, 7000, 0, 10]  # Right-hand side values for the constraints
    
    bounds = [(0, None), (0, None)]  # Non-negativity constraints for x and y
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    return res.fun