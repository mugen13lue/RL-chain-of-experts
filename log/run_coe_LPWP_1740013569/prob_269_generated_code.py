from scipy.optimize import linprog

def prob_269():
    c = [-3, -10]  # Coefficients of the objective function to maximize 3x + 10y

    A = [[3, 0],  # Coefficients of the constraints
         [0, 10],
         [-1, -1],
         [0, -1]]
    
    b = [200, 200, -4, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(4, None))  # Using linear programming to maximize the objective function

    return res.fun * -1  # Return the negative of the optimized objective function value to maximize mail delivery