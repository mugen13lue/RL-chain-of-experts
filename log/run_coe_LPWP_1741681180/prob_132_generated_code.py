from scipy.optimize import linprog

def prob_132(table_1, table_2):
    c = [-4, -5]  # coefficients for maximizing slime production
    A = [[3, 8], [5, 6]]  # coefficients for powder and glue constraints
    b = [100, 90]  # available powder and glue
    A_eq = [[-2, -4]]  # coefficients for mess constraint
    b_eq = [-30]  # maximum mess allowed

    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=(0, None))

    return res.x