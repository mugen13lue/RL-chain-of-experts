from scipy.optimize import minimize

def prob_217(cat_paw, gold_shark, cat_paw_percentage_first_mix, gold_shark_percentage_first_mix,
             cat_paw_percentage_second_mix, gold_shark_percentage_second_mix, cat_paw_limit, gold_shark_limit,
             profit_first_mix, profit_second_mix):
    
    # Define the objective function to maximize profit
    def objective(x):
        cat_paw = x[0]
        gold_shark = x[1]
        return -(cat_paw * profit_first_mix + gold_shark * profit_second_mix)
    
    # Define the constraints
    def constraint1(x):
        cat_paw = x[0]
        gold_shark = x[1]
        return cat_paw * cat_paw_percentage_first_mix + gold_shark * gold_shark_percentage_first_mix - cat_paw_limit
    
    def constraint2(x):
        cat_paw = x[0]
        gold_shark = x[1]
        return cat_paw * cat_paw_percentage_second_mix + gold_shark * gold_shark_percentage_second_mix - gold_shark_limit
    
    # Define the bounds for cat paw and gold shark snacks
    bounds = [(0, cat_paw_limit), (0, gold_shark_limit)]
    
    # Use scipy minimize function to find the optimal solution
    result = minimize(objective, [0, 0], bounds=bounds, constraints=({'type': 'ineq', 'fun': constraint1},
                                                                     {'type': 'ineq', 'fun': constraint2}))
    
    return -result.fun