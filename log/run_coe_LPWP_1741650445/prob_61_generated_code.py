import gurobipy as gp
from gurobipy import GRB

def prob_61(new_model, old_model):
    """
    Args:
        new_model: an integer, the number of new model furnaces
        old_model: an integer, the number of old model furnaces

    Returns:
        obj: a float, the objective value
    """
    obj = 0
    
    # Create a new model
    m = gp.Model("furnace_purchase")

    # Define decision variables
    x = m.addVar(lb=5, vtype=GRB.INTEGER, name="new_model")
    y = m.addVar(vtype=GRB.INTEGER, name="old_model")

    # Set objective function
    m.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    m.addConstr(y <= 0.35*(x + y), "old_model_limit")
    m.addConstr(10*x + 15*y >= 200, "apartments_requirement")
    m.addConstr(200*x + 250*y <= 3500, "electricity_requirement")

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    obj = m.objVal

    return obj