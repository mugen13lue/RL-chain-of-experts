def prob_71(top_loading_model, front_loading_model, var1, var2, var3, var4):
    """
    Args:
        top_loading_model: an integer, representing the number of top-loading machines
        front_loading_model: an integer, representing the number of front-loading machines
        var1: an integer, representing the number of items the top-loading model can wash per day
        var2: an integer, representing the number of items the front-loading model can wash per day
        var3: an integer, representing the amount of energy consumed by the top-loading model per day
        var4: an integer, representing the amount of energy consumed by the front-loading model per day
    Returns:
        obj: an integer, representing the minimum total number of washing machines
    """
    
    from scipy.optimize import linprog

    c = [1, 1]  # Coefficients of the objective function to minimize x + y

    A = [[-var1, -var2], [var3, var4], [-1, -1], [0, -1], [0.4, 0], [0, 1]]
    b = [-5000, 7000, 0, -10, 0, 0]

    bounds = [(0, None), (0, None)]

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(res.fun)  # Minimum total number of washing machines