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
    # Create a new model
    model = gp.Model("shipping_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of large ships
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of small ships

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x <= y)
    model.addConstr(500*x + 200*y >= 3000)
    model.addConstr(x >= 0)
    model.addConstr(y >= 0)

    # Optimize model
    model.optimize()

    # Get the objective value
    objective_value = model.objVal

    return objective_value