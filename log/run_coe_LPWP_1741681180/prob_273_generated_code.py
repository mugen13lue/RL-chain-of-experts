from scipy.optimize import minimize

def prob_273(camel_caravans, desert_trucks):
    """
    Args:
        camel_caravans: an integer, the number of camel caravans
        desert_trucks: an integer, the number of desert trucks
        
    Returns:
        total_number_of_hours: an integer, the total number of hours required
    """
    def objective_function(x):
        return 12 * x[0] + 5 * x[1]  # Total hours
        
    def constraint(x):
        return 50 * x[0] + 150 * x[1] - 1500  # Total units of goods
        
    initial_guess = [camel_caravans, desert_trucks]
    bounds = [(0, None), (0, None)]
    constraints = {'type': 'ineq', 'fun': constraint}
    
    result = minimize(objective_function, initial_guess, bounds=bounds, constraints=constraints)
    
    total_number_of_hours = result.fun
    return total_number_of_hours