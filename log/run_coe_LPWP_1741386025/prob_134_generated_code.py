from scipy.optimize import linprog

def prob_134(cheesecake, caramel_cake, cheesecake_calories, cheesecake_sugar, caramel_cake_calories, caramel_cake_sugar, min_caramel_cake_slices, max_calories):
    c = [-cheesecake_sugar, -caramel_cake_sugar]  # Coefficients for maximizing sugar consumption
    A = [[-cheesecake_calories, -caramel_cake_calories]]  # Coefficients for total calories constraint
    b = [-max_calories]  # Maximum calories constraint
    A_eq = [[1, -3], [0, 1]]  # Coefficients for minimum slices constraints
    b_eq = [0, min_caramel_cake_slices]  # Minimum slices constraints

    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=(0, None))

    total_amount_of_sugar = -res.fun  # Maximum total amount of sugar consumed

    return total_amount_of_sugar