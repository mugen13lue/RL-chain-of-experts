from scipy.optimize import linprog

def prob_216():
    c = [12, 10, 15]  # Coefficients of the objective function to maximize (12x1 + 10x2 + 15x3)
    A = [[400, 500, 450], [200, 300, 350]]  # Coefficients of the inequality constraints
    b = [20000, 14000]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None), (0, None)]  # Bounds for the decision variables x1, x2, x3

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    if res.success:
        x1, x2, x3 = res.x
        profit = res.fun  # Maximum profit achieved
        return profit, x1, x2, x3
    else:
        return "Optimization failed. Check constraints."

profit, crepe_cakes, sponge_cakes, birthday_cakes = prob_216()
print(f"Maximum profit: ${profit:.2f}")
print(f"Number of crepe cakes: {crepe_cakes}")
print(f"Number of sponge cakes: {sponge_cakes}")
print(f"Number of birthday cakes: {birthday_cakes}")