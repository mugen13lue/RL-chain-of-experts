from scipy.optimize import linprog

def prob_278():
    c = [1, 1]  # Coefficients of the objective function to minimize (sedans + buses)
    A = [[-50, -250], [10, 40]]  # Coefficients of the inequality constraints
    b = [-4600, 800]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    sedans = round(res.x[0])
    buses = round(res.x[1])

    return sedans, buses

sedans, buses = prob_278()
print("Number of sedans to purchase:", sedans)
print("Number of buses to purchase:", buses)