from scipy.optimize import linprog

def prob_81(motion_activated, manual, motion_activated_drops, motion_activated_power, manual_drops, manual_power, manual_limit, capacity, power_limit):
    c = [1, 1]  # Coefficients for the objective function to minimize total number of machines
    A = [
        [-1, 0],  # x >= 3
        [-0.4, -0.4],  # y <= 0.4(x+y)
        [-motion_activated_drops, -manual_drops],  # -50x - 75y <= -1000
        [motion_activated_power, manual_power]  # 30x + 20y <= 500
    ]
    b = [-3, 0, -1000, 500]  # Right-hand side values for constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun