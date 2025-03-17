def prob_86(mocha_coffee_powder, mocha_milk, regular_coffee_powder, regular_milk, mocha_time, regular_time,
            mocha_regular_ratio, coffee_powder_limit, milk_limit):
    
    from scipy.optimize import linprog

    c = [mocha_time, regular_time]
    A = [[mocha_coffee_powder, regular_coffee_powder], [mocha_milk, regular_milk], [-1, 3]]
    b = [coffee_powder_limit, milk_limit, 0]

    res = linprog(c, A_ub=A, b_ub=b)
    
    return res.fun