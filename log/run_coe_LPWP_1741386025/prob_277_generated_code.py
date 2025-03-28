def prob_277(mechanical, standard_keyboards):
    """
    Args:
        mechanical: an integer, the number of mechanical keyboards
        standard_keyboards: an integer, the number of standard keyboards
    Returns:
        obj: an integer, the maximum total number of keyboards manufactured
    """
    
    from scipy.optimize import linprog

    c = [-1, -1]  # Coefficients of the objective function to maximize x + y
    A = [[5, -2], [2, -1]]  # Coefficients of the inequality constraints
    b = [1000, 250]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (30, None)]  # Bounds for x and y
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    if res.success:
        obj = -res.fun  # Maximum total number of keyboards manufactured
    else:
        obj = "No feasible solution found"
    
    return obj