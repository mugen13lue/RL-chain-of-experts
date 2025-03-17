from scipy.optimize import linprog

def prob_37(mango_cost, guava_cost):
    c = [-3, -4]  # Coefficients of the objective function to maximize 3x + 4y
    A = [[5, 3], [-3, -4], [-1, 0], [1, 0], [-1/3, -1]]  # Coefficients of the constraints
    b = [20000, 0, -100, 150, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    max_profit = -res.fun  # Maximum profit is the negative of the minimum value found by linprog

    return max_profit