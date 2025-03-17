from scipy.optimize import linprog

def prob_181():
    c = [30, 25]  # Coefficients of the objective function (gas used for submarine and boat)
    A = [[100, 80], [-1, -1], [0, -1]]  # Coefficients of the inequality constraints
    b = [1000, -6, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, 6), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun

# No test code is required outside the function

# The final code effectively implements the linear programming problem to minimize the total amount of gas used while satisfying the given constraints.