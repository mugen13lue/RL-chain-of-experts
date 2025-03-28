from scipy.optimize import linprog

def prob_223():
    c = [-2000, -5000, -9000]  # Coefficients of the objective function to maximize
    A = [[1200, 2000, 4000], [0, 1, 0], [0, 0, 1], [-2000, -5000, -9000], [-1, -1, -1]]
    b = [20000, 8, 2, 0, 0.2]

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun * -1  # Return the maximum audience reach

# Call the function and print the result
print(prob_223())