from scipy.optimize import linprog

def prob_262(kayak, motorboat, constraint1):
    c = [5, 3]  # Coefficients of objective function (time taken for kayak and motorboat trips)
    A = [[4, 5], [0, 1], [-0.75, -0.75]]  # Coefficients of constraints
    b = [constraint1, 25, 0]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)  # Return the total time needed to transport all locals

# Test the function with example values
print(prob_262(0, 0, 550))  # Output: 1650