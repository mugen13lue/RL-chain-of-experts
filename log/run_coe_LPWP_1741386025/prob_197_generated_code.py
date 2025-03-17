from scipy.optimize import linprog

def prob_197(small_canoes, smaller_diesel_boats):
    """
    Args:
        small_canoes: an integer, the number of small canoes used
        smaller_diesel_boats: an integer, the number of smaller diesel boats used
        
    Returns:
        total_number_of_canoes_and_diesel_boats: an integer, the total number of canoes and diesel boats needed
    """
    c = [1, 1]  # Coefficients for the objective function to minimize Z = x + y
    A = [[-10, -15], [1, -3]]  # Coefficients for the constraints
    b = [-1000, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    total_number_of_canoes_and_diesel_boats = res.x[0] + res.x[1]
    
    return int(total_number_of_canoes_and_diesel_boats)