from scipy.optimize import linprog

def prob_229(low_power, high_power):
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y

    A = [
        [-12, -17],  # Coefficients of the Cooling Capacity Constraint: 12x + 17y >= 250
        [150, 250],  # Coefficients of the Electricity Constraint: 150x + 250y <= 3400
        [-1, 0.3],   # Coefficients of the Percentage Constraint: x <= 0.3(x+y)
        [0, -1]      # Coefficients of the Minimum High-powered Constraint: y >= 7
    ]

    b = [-250, 3400, 0, -7]  # Right-hand side values of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun  # Total number of air conditioners