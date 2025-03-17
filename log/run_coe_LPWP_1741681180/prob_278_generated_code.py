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

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="sedans")
    x2 = model.addVar(vtype=GRB.INTEGER, name="buses")

    # Set objective
    model.setObjective(x1 + x2, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x1 + 40*x2 <= 800, "pollution_constraint")
    model.addConstr(50*x1 + 250*x2 >= 4600, "customer_constraint")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj