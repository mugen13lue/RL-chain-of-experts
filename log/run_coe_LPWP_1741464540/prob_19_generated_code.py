from scipy.optimize import linprog

def prob_19(thin_jar, stubby_jar):
    c = [-5, -9]  # Coefficients of the objective function to minimize (-5x - 9y)
    A = [[50, 30], [90, 150]]  # Coefficients of the left-hand side of the inequalities
    b = [3000, 4000]  # Right-hand side of the inequalities
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraint)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    if res.success:
        max_profit = -res.fun  # Maximum profit is the negative of the minimum value obtained
        return int(max_profit)
    else:
        return "No feasible solution found."