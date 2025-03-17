from scipy.optimize import linprog

def minimize_sleep_medicine(daytime_pills, nighttime_pills, total_painkiller_units, daytime_painkiller_units, daytime_sleep_units, nighttime_painkiller_units, nighttime_sleep_units, min_nighttime_pills, min_daytime_ratio):
    c = [daytime_sleep_units, nighttime_sleep_units]
    A = [[daytime_painkiller_units, nighttime_painkiller_units],
         [daytime_sleep_units, nighttime_sleep_units],
         [-1, 0],
         [0, -1],
         [-0.4, -0.4]]
    b = [total_painkiller_units, float('inf'), 0, min_nighttime_pills, 0]

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    daytime_pills_optimal = res.x[0]
    nighttime_pills_optimal = res.x[1]

    return daytime_pills_optimal, nighttime_pills_optimal, res.fun

# Given parameters
daytime_pills = 0
nighttime_pills = 0
total_painkiller_units = 800
daytime_painkiller_units = 6
daytime_sleep_units = 2
nighttime_painkiller_units = 5
nighttime_sleep_units = 5
min_nighttime_pills = 200
min_daytime_ratio = 0.4

daytime_pills_optimal, nighttime_pills_optimal, min_sleep_medicine = minimize_sleep_medicine(daytime_pills, nighttime_pills, total_painkiller_units, daytime_painkiller_units, daytime_sleep_units, nighttime_painkiller_units, nighttime_sleep_units, min_nighttime_pills, min_daytime_ratio)

print("Optimal number of daytime pills:", daytime_pills_optimal)
print("Optimal number of nighttime pills:", nighttime_pills_optimal)
print("Minimum amount of sleep medicine required:", min_sleep_medicine)