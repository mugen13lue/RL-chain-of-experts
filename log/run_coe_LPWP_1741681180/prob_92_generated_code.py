def prob_92(medium_sized_factory, small_factory):
    """
    Args:
        medium_sized_factory: an integer, the number of medium-sized factories
        small_factory: an integer, the number of small factories

    Returns:
        obj: an integer, the objective value
    """
    obj = medium_sized_factory + small_factory
    return obj

# Constraints
toy_constraint = 250
operator_constraint = 16

# Solve the linear programming problem
from scipy.optimize import linprog

# Coefficients of the objective function
c = [1, 1]

# Coefficients of the inequality constraints
A = [[-50, -35], [3, 2]]
b = [-toy_constraint, operator_constraint]

# Bounds for variables
x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the optimal values
optimal_values = res.x
optimal_obj = res.fun

# Print the optimal values
print("Number of medium-sized factories to build:", round(optimal_values[0]))
print("Number of small factories to build:", round(optimal_values[1]))
print("Objective value (total number of factories):", round(optimal_obj))