import gurobipy as gp
from gurobipy import GRB

def prob_196(large_ships, small_ships):
    """
    Args:
        large_ships: an integer, number of large ships
        small_ships: an integer, number of small ships
    Returns:
        objective_value: an integer, the objective value
    """
    m = gp.Model("shipping_problem")

    # Decision variables
    num_large_ships = m.addVar(vtype=GRB.INTEGER, name="num_large_ships")
    num_small_ships = m.addVar(vtype=GRB.INTEGER, name="num_small_ships")

    # Objective function: minimize the total number of ships used
    m.setObjective(num_large_ships + num_small_ships, sense=GRB.MINIMIZE)

    # Constraints
    m.addConstr(500*num_large_ships + 200*num_small_ships >= 3000, "min_containers")
    m.addConstr(num_large_ships <= num_small_ships, "large_small_ships")

    # Optimize model
    m.optimize()

    # Get the objective value
    objective_value = m.objVal

    return objective_value