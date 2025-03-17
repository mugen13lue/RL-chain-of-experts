def prob_86(mocha_coffee_powder, mocha_milk, regular_coffee_powder, regular_milk, mocha_time, regular_time,
            mocha_regular_ratio, coffee_powder_limit, milk_limit):
    
    from scipy.optimize import linprog

    # Coefficients of the objective function
    c = [mocha_time, regular_time]

    # Coefficients of the inequality constraints
    A = [[mocha_coffee_powder, regular_coffee_powder],
         [mocha_milk, regular_milk],
         [-1, 3]]

    # Right-hand side of the inequality constraints
    b = [coffee_powder_limit, milk_limit, 0]

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    return int(res.fun)