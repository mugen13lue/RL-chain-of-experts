from scipy.optimize import linprog

def prob_133(daytime_pills, nighttime_pills, total_painkiller_units, daytime_painkiller_units, daytime_sleep_units, nighttime_painkiller_units, nighttime_sleep_units, min_nighttime_pills, min_daytime_ratio):
    c = [daytime_sleep_units, nighttime_sleep_units]  # Coefficients of the objective function Z = daytime_sleep_units * x + nighttime_sleep_units * y
    A = [[daytime_painkiller_units, nighttime_painkiller_units], [daytime_sleep_units, nighttime_sleep_units], [-min_daytime_ratio, 1], [0, 1]]  # Coefficients of the constraints
    b = [total_painkiller_units, 0, 0, min_nighttime_pills]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun