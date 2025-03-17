from scipy.optimize import linprog

def prob_86(mocha_coffee_powder, mocha_milk, regular_coffee_powder, regular_milk, mocha_time, regular_time,
            mocha_regular_ratio, coffee_powder_limit, milk_limit):
    
    c = [mocha_time, regular_time]  # Coefficients of the objective function to minimize total production time

    A = [[mocha_coffee_powder, regular_coffee_powder], [mocha_milk, regular_milk], [-1, 3]]  # Coefficients of the constraints
    b = [coffee_powder_limit, milk_limit, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')  # Using linear programming to minimize the objective function

    return res.fun  # Return the minimum total production time