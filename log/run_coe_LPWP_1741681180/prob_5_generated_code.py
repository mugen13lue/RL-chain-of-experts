from scipy.optimize import linprog

def prob_5():
    c = [-0.01, -0.03]  # Coefficients of the objective function to maximize profit
    A = [[1, 1], [-3, 1], [0, 1]]  # Coefficients of the inequality constraints
    b = [100000, 0, 70000]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])
    
    profit = -res.fun  # Maximum profit
    healthcare = res.x[0]  # Amount invested in healthcare
    telecom = res.x[1]  # Amount invested in telecom

    return profit, healthcare, telecom

profit, healthcare, telecom = prob_5()
print("Maximum Profit: $", round(profit, 2))
print("Amount to Invest in Healthcare: $", round(healthcare, 2))
print("Amount to Invest in Telecom: $", round(telecom, 2))