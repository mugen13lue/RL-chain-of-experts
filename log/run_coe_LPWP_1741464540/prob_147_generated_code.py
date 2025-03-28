from scipy.optimize import linprog

def prob_147(beam_bridges, truss_bridges):
    c = [-40, -60]  # Coefficients of the objective function to maximize -40x - 60y

    A = [[30, 50],  # Coefficients of the inequality constraints
         [5, 8],
         [0, -1],
         [-1, 0]]
    
    b = [600,  # Right-hand side values of the inequality constraints
         100,
         -5,
         0]

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum total mass that can be supported