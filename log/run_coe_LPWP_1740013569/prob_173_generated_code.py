from scipy.optimize import linprog

def prob_173(van, minibus):
    """
    Args:
        van: an integer, represents the number of vans used
        minibus: an integer, represents the number of minibuses used
    Returns:
        obj: an integer, the total amount of pollution produced
    """
    obj = 7 * van + 10 * minibus
    return obj

# Constraints
kids_constraint = [-6, -10]
minibuses_constraint = [0, -1]
vans_constraint = [1, 0]

# Coefficients for the objective function
c = [7, 10]

# Coefficients for the inequality constraints
A = [kids_constraint, minibuses_constraint, vans_constraint]
b = [-150, -10, 0]

# Bounds for the variables
x_bounds = (0, None)
y_bounds = (0, 10)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the optimal values
optimal_van = res.x[0]
optimal_minibus = res.x[1]
optimal_pollution = prob_173(optimal_van, optimal_minibus)

print("Optimal number of vans:", optimal_van)
print("Optimal number of minibuses:", optimal_minibus)
print("Total pollution produced:", optimal_pollution)