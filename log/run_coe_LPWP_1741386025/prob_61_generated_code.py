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
    
    # Create a new model
    model = gp.Model("furnace_purchase")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="new_model")
    y = model.addVar(vtype=GRB.INTEGER, name="old_model")
    
    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(10*x + 15*y >= 200, "apartments_constraint")
    model.addConstr(200*x + 250*y <= 3500, "electricity_constraint")
    model.addConstr(y <= 0.35*(x + y), "percentage_constraint")
    model.addConstr(x >= 5, "min_new_model_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj