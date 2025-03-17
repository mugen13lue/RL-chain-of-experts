from scipy.optimize import linprog

def prob_37(mango_cost, guava_cost):
    c = [-3, -4]  # Coefficients of the objective function to maximize profit: 3x + 4y

    A = [[5, 3], [-1, 0], [1, 0], [0, -1/3]]  # Coefficients of the inequality constraints
    b = [20000, -100, 150, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    return -res.fun  # Return the maximum profit