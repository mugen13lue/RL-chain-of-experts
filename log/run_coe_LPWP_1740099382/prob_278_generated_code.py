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
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="sedans")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="buses")

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 250*y >= 4600)
    model.addConstr(10*x + 40*y <= 800)

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj