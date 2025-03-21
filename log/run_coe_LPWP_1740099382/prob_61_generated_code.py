import gurobipy as gp
from gurobipy import GRB

def prob_61():
    """
    Returns:
        obj: a float, the objective value
    """
    # Create a new model
    model = gp.Model("furnace_purchase")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="new_model")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="old_model")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 15*y >= 200, "apartments")
    model.addConstr(200*x + 250*y <= 3500, "electricity")
    model.addConstr(y <= 0.35*(x+y), "percentage")
    model.addConstr(x >= 5, "minimum_new_model")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj