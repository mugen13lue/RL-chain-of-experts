from scipy.optimize import linprog

def prob_66(almond_croissants, pistachio_croissants, butter_units, flour_units, production_time):
    c = [12, 10]
    A = [[5, 3], [8, 6], [-1, 3]]
    b = [butter_units, flour_units, 0]
    x_bounds = (0, None)
    y_bounds = (0, None)

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])

    optimal_x = res.x[0]
    optimal_y = res.x[1]

    return int(optimal_x), int(optimal_y)