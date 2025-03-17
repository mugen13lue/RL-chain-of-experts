def prob_273(camel_caravans, desert_trucks):
    """
    Args:
        camel_caravans: an integer, the number of camel caravans
        desert_trucks: an integer, the number of desert trucks
        
    Returns:
        total_number_of_hours: an integer, the total number of hours required
    """
    
    # Objective function: minimize total number of hours
    # Total number of hours = 12x + 5y
    total_number_of_hours = 12*camel_caravans + 5*desert_trucks
    
    return total_number_of_hours

# Given the constraints: 50x + 150y >= 1500
# We need to find the optimal values for x and y that satisfy the constraints and minimize the total number of hours

# Let's solve the optimization problem using linear programming libraries in Python such as PuLP or scipy.optimize

# Import the necessary libraries
from scipy.optimize import linprog

# Coefficients of the objective function
c = [12, 5]

# Coefficients of the inequality constraints
A = [[-50, -150]]

# Right-hand side of the inequality constraints
b = [-1500]

# Bounds for x and y (non-negative values)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Get the optimal values for x and y
optimal_x = res.x[0]
optimal_y = res.x[1]

# Calculate the total number of hours required with the optimal values
total_hours = prob_273(int(optimal_x), int(optimal_y))

print("Optimal number of camel caravans:", int(optimal_x))
print("Optimal number of desert trucks:", int(optimal_y))
print("Total number of hours required:", total_hours)