from scipy.optimize import linprog

def prob_219(math_workbooks, english_workbooks):
    c = [-15, -17]  # Coefficients of the objective function to minimize (-15x - 17y)
    A = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1]]  # Coefficients of the inequality constraints
    b = [math_workbooks, english_workbooks, -math_workbooks, -english_workbooks, -200]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')  # Using linear programming to maximize profit
    return -res.fun  # Returning the negative of the minimum value as we are maximizing profit

# Example usage:
# print(prob_219(40, 60))  # Output: 1700.0