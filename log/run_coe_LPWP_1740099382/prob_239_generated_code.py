import gurobipy as gp
from gurobipy import GRB

def prob_239():
    """
    Returns:
        obj: an integer, total number of limousines and buses used
    """
    
    # Create a new model
    model = gp.Model("transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="limousines")
    y = model.addVar(vtype=GRB.INTEGER, name="buses")

    # Set objective function: minimize total number of vehicles used
    model.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(12*x + 18*y >= 400, "total_people")
    model.addConstr(x >= 0.7*(x+y), "limousine_percentage")

    # Optimize model
    model.optimize()

    # Get the total number of limousines and buses used
    obj = model.objVal

    return obj