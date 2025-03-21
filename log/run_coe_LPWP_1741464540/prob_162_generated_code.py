from scipy.optimize import linprog

def prob_162(bus, car):
    """
    Args:
        bus: an integer (number of bus trips)
        car: an integer (number of car trips)
    
    Returns:
        obj: an integer (total time required to transport the monkeys)
    """
    
    c = [30, 15]  # Coefficients of the objective function (time)
    A = [[20, 6], [-1, -0.6]]  # Coefficients of the constraints
    b = [300, 0]  # Right-hand side of the constraints
    bounds = [(0, 10), (0, None)]  # Bounds for the variables
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    obj = res.fun  # Total time required
    return obj