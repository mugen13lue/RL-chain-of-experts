def prob_151(ships, planes):
    """
    Args:
        ships: an integer, representing the number of ship trips
        planes: an integer, representing the number of plane trips
    Returns:
        obj: an integer, representing the total amount of fuel consumed
    """
    obj = 500 * ships + 300 * planes
    return obj

# Constraints
def total_containers_constraint(ships, planes):
    return 40 * ships + 20 * planes >= 500

def fuel_consumption_ships_constraint(ships):
    return 500 * ships

def fuel_consumption_planes_constraint(planes):
    return 300 * planes

def max_plane_trips_constraint(planes):
    return planes <= 10

def min_ship_trips_constraint(ships, planes):
    return ships >= 0.5 * (ships + planes)

# Objective function
def minimize_fuel_consumption(ships, planes):
    return 500 * ships + 300 * planes

# Solve the problem
def solve_problem():
    from scipy.optimize import linprog

    c = [500, 300]  # Coefficients of the objective function to minimize
    A = [[-40, -20], [-500, 0], [0, -300], [0, 1], [-0.5, -0.5]]  # Coefficients of the constraints
    b = [-500, -500, -300, 10, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    return res

# Call the solve_problem function to get the optimal solution
result = solve_problem()
print(result)