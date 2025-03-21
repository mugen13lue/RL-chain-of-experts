from scipy.optimize import linprog

def prob_69(brownies, lemon_squares):
    """
    Args:
        brownies: an integer, the number of brownies to be made
        lemon_squares: an integer, the number of lemon squares to be made
        
    Returns:
        obj: an integer, the total amount of fiber needed
    """
    obj = 4 * brownies + 6 * lemon_squares
    return obj

# Constraints
def chocolate_mix_constraint(brownies, lemon_squares):
    return 5 * brownies + 7 * lemon_squares <= 2500

def lemon_mix_constraint(brownies, lemon_squares):
    return 4 * brownies + 6 * lemon_squares <= 3300

def lemon_squares_greater_than_brownies(brownies, lemon_squares):
    return lemon_squares >= brownies

def non_negativity_constraint(brownies, lemon_squares):
    return brownies >= 0 and lemon_squares >= 0

def at_least_40_percent_brownies(brownies, lemon_squares):
    return brownies >= 0.4 * (brownies + lemon_squares)

# Minimize total amount of fiber needed
c = [4, 6]  # Coefficients of the objective function to minimize
A = [[5, 7], [4, 6], [-1, 1], [-1, 0], [0, -1], [-0.4, -0.4]]  # Coefficients of the inequality constraints
b = [2500, 3300, 0, 0, 0, 0]  # Right-hand side of the inequality constraints

res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

brownies_optimal = round(res.x[0])
lemon_squares_optimal = round(res.x[1])

fiber_needed = prob_69(brownies_optimal, lemon_squares_optimal)

print("Optimal number of brownies to be made:", brownies_optimal)
print("Optimal number of lemon squares to be made:", lemon_squares_optimal)
print("Total amount of fiber needed:", fiber_needed)