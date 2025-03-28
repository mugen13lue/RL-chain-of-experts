def prob_150(small_bottles, large_bottles):
    """
    Args:
        small_bottles: an integer, the number of small bottles
        large_bottles: an integer, the number of large bottles
        
    Returns:
        amount_of_honey: an integer, the maximum amount of honey that can be transported
    """
    
    # Objective function: maximize Z = 5x + 20y
    # Subject to constraints:
    # x <= 300
    # y <= 100
    # x + y <= 200
    # x >= 2y
    # y >= 50
    
    from scipy.optimize import linprog
    
    c = [-5, -20]  # Coefficients of the objective function to be minimized
    
    A = [[1, 0], [0, 1], [1, 1], [-2, 1], [0, -1]]  # Coefficients of the inequality constraints
    b = [300, 100, 200, 0, -50]  # Right-hand side of the inequality constraints
    
    res = linprog(c, A_ub=A, b_ub=b)
    
    amount_of_honey = -res.fun  # Maximum amount of honey transported
    
    return int(amount_of_honey)