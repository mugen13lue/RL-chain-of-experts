from scipy.optimize import linprog

def prob_17(chair, dresser, constraint1, constraint2):
    c = [-43, -52]  # Coefficients of the objective function to minimize (-43x - 52y)
    A = [[1.4, 1.1], [2, 3]]  # Coefficients of the constraints
    b = [constraint1, constraint2]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    max_profit = -res.fun  # Maximum profit is the negative of the minimum value obtained by linprog

    return max_profit