from scipy.optimize import linprog

def prob_211():
    c = [-2.1, -3.3]  # Coefficients of the objective function to minimize (-2.1x - 3.3y)
    A = [[-1, 0], [0, -1], [1, 1]]  # Coefficients of the inequality constraints
    b = [-15000, -5000, 50000]  # Right-hand side of the inequality constraints
    bounds = [(0, 40000), (0, 20000)]  # Bounds for x and y (laminate planks and carpets)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    max_profit = -res.fun  # Maximum profit achieved
    laminate_planks = res.x[0]  # Number of laminate planks produced weekly
    carpets = res.x[1]  # Number of carpets produced weekly

    return max_profit, laminate_planks, carpets

max_profit, laminate_planks, carpets = prob_211()
print(f"Maximum profit: ${max_profit}")
print(f"Number of laminate planks produced weekly: {laminate_planks} square feet")
print(f"Number of carpets produced weekly: {carpets} square feet")