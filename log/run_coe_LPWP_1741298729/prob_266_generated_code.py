from scipy.optimize import linprog

def prob_266(acai_berry_smoothie, banana_chocolate_smoothie):
    c = [3, 4]  # Coefficients of the objective function to minimize total amount of water used
    A = [[7, 0], [0, 6], [3, 4], [-0.65, -0.35], [-1, 1]]  # Coefficients of the constraints
    b = [3500, 3200, 12000, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    if res.success:
        amount_of_water = res.fun
        return amount_of_water
    else:
        return "Optimization failed"