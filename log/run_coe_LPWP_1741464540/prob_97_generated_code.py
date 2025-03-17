from scipy.optimize import linprog

def prob_97(premium_model, regular_model):
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y

    A = [
        [-30, -20],  # Coefficients of PagesPrinted constraint: 30x + 20y >= 200
        [4, 3],      # Coefficients of InkUsed constraint: 4x + 3y <= 35
        [-1, 1]      # Coefficients of PremiumRegularRelation constraint: x >= y
    ]

    b = [-200, 35, 0]  # Right-hand side values of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    return int(res.x[0]), int(res.x[1])