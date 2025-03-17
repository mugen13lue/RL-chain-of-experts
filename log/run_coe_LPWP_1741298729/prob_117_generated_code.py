from scipy.optimize import linprog

def prob_117(burgers, pizza):
    """
    Args:
        burgers: an integer, the number of burgers
        pizza: an integer, the number of pizza slices
    Returns:
        obj: an integer, the objective value (cholesterol intake)
    """
    c = [12, 10]  # Coefficients of the objective function to minimize cholesterol intake
    A = [[-10, -8], [-300, -250], [12, 10], [-1, 2]]  # Coefficients of the inequality constraints
    b = [-130, -3000, 0, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res.fun