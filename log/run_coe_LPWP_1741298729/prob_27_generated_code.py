from scipy.optimize import linprog

def prob_27(model_trains, planes, wood_train, paint_train, wood_plane, paint_plane, wood_available, paint_available):
    c = [-8, -10]  # Coefficients of the objective function to be maximized (-8x - 10y)
    A = [[3, 4], [3, 2]]  # Coefficients of the left-hand side of the inequalities
    b = [wood_available, paint_available]  # Right-hand side of the inequalities

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return round(-res.fun)  # Return the maximum profit