import gurobipy as gp
from gurobipy import GRB

def prob_187():
    """
    Returns:
        obj: an integer, the objective value
    """
    
    # Create a new model
    model = gp.Model("corn_transportation")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of ferry trips
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of light rail trips
    
    # Set objective function: Minimize Z = x + y
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(20*x + 15*y >= 500, "trip_constraint")  # Trip constraint
    model.addConstr(y >= 4*x, "light_rail_constraint")  # Light rail constraint
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj