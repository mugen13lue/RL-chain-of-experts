from scipy.optimize import linprog

def prob_103(small_bone, large_bone, medication_constraint, small_bone_percentage_constraint, minimum_large_bone_constraint):
    c = [12, 15]  # Coefficients of the objective function (meat needed)
    A = [[10, 15], [-1, 0], [1, 0], [1, 1]]  # Coefficients of the inequality constraints
    b = [medication_constraint, 0, 0, 0.5*(small_bone_percentage_constraint + minimum_large_bone_constraint)]
    bounds = [(0, None), (minimum_large_bone_constraint, None)]  # Bounds for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    amount_of_meat = res.fun  # Optimal value of the objective function

    return amount_of_meat