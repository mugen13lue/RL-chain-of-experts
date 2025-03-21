from scipy.optimize import linprog

def prob_224():
    c = [-1, -1]  # Coefficients of the objective function to maximize (-T - B)
    A = [[5, -1], [2, 10], [0, -1]]  # Coefficients of the constraints
    b = [0, 22000, -45]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)  # Solving the linear programming problem

    temperature_check = res.x[0]  # Number of temperature checks
    blood_test = res.x[1]  # Number of blood tests

    return temperature_check, blood_test

temperature_check, blood_test = prob_224()
print(f"Number of temperature checks: {temperature_check}")
print(f"Number of blood tests: {blood_test}")