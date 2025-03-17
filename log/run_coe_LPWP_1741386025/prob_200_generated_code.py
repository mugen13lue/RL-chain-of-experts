from scipy.optimize import linprog

def prob_200(hams, pork_ribs):
    c = [-150, -300]  # Coefficients of the objective function to maximize profit
    A = [[4, 2.5], [2, 3.5]]  # Coefficients of the constraints
    b = [4000, 4000]  # RHS of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return -res.fun  # Return the maximum profit