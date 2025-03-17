import gurobipy as gp
from gurobipy import GRB

def prob_258(process_J, process_P):
    """
    Args:
        process_J: an integer, number of process J performed
        process_P: an integer, number of process P performed
    Returns:
        obj: an integer, the objective value (amount of metal extracted)
    """
    # Create a new model
    model = gp.Model("metal_extraction")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="process_J")
    y = model.addVar(vtype=GRB.INTEGER, name="process_P")

    # Set objective function
    model.setObjective(5*x + 9*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(8*x + 6*y <= 1500, "water_constraint")
    model.addConstr(3*x + 5*y <= 1350, "pollution_constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj