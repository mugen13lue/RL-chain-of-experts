from scipy.optimize import linprog

def prob_214(basketball_tournament, horse_race, soccer_game, limit_1, limit_2):
    c = [-1.2, -0.5, -0.1]  # Coefficients of the objective function to maximize
    A = [[1, 1, 1], [0.5, 0.25, 0.1]]  # Coefficients of the constraints
    b = [100000, 30]  # Right-hand side of the constraints

    res = linprog(c, A_eq=A, b_eq=b, bounds=[(0, None), (0, None), (0, None)])

    return -res.fun  # Return the maximum average payout