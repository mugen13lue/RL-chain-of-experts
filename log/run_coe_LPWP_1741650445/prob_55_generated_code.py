import gurobipy as gp
from gurobipy import GRB

def prob_55(windrower, hay_harvester):
    """
    Args:
        windrower: an integer,
        hay_harvester: an integer,
    Returns:
        obj: an integer,
    """
    # Create a new model
    model = gp.Model("hay_processing")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(10*x + 8*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(10*x + 8*y <= 200)
    model.addConstr(5*x + 3*y <= 800)
    model.addConstr(2*x + y <= 300)

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj