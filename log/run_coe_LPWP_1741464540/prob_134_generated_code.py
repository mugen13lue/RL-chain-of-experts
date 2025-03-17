from scipy.optimize import linprog

def prob_134(cheesecake, caramel_cake, cheesecake_calories, cheesecake_sugar, caramel_cake_calories, caramel_cake_sugar, min_caramel_cake_slices, max_calories):
    c = [-cheesecake_sugar, -caramel_cake_sugar]  # Coefficients of the objective function to maximize sugar consumption

    A = [[-1, 0],  # Coefficients of x in constraints
         [0, -1],  # Coefficients of y in constraints
         [cheesecake_calories, caramel_cake_calories]]  # Coefficients of calories in constraints

    b = [-min_caramel_cake_slices, -3, max_calories]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    total_amount_of_sugar = -res.fun  # Maximum total amount of sugar consumed

    return total_amount_of_sugar