from scipy.optimize import linprog

def prob_200(hams, pork_ribs):
    c = [-150, -300]  # Coefficients of the objective function to minimize (-150x - 300y)
    A = [[4, 2.5], [2, 3.5]]  # Coefficients of the constraints
    b = [4000, 4000]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    if res.success:
        max_profit = -res.fun  # Maximum profit achieved
        return max_profit
    else:
        return "Optimization failed"