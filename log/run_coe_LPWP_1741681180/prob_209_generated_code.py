from scipy.optimize import linprog

def prob_209(regular_brand, premium_brand):
    c = [20, 35]  # Cost coefficients for regular and premium brands
    A = [[-4, -12], [-7, -10], [-10, -16]]  # Coefficients for calcium, vitamin mix, and protein constraints
    b = [-15, -20, -20]  # Minimum requirements for calcium, vitamin mix, and protein

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)