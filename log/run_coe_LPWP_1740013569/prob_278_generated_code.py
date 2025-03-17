import gurobipy as gp
from gurobipy import GRB

def prob_278(sedans, buses):
    """
    Args:
        sedans: an integer representing the number of sedans.
        buses: an integer representing the number of buses.
    Returns:
        obj: an integer representing the objective value (total number of vehicles).
    """
    # Create a new model
    model = gp.Model("vehicle_purchase")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="sedans")
    y = model.addVar(vtype=GRB.INTEGER, name="buses")

    # Set objective function: minimize total number of vehicles
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 40*y <= 800, "pollution")
    model.addConstr(50*x + 250*y >= 4600, "customers")
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj