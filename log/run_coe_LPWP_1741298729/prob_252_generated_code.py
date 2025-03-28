import gurobipy as gp
from gurobipy import GRB

def prob_252(large_mobile_production_units, small_mobile_production_units):
    """
    Args:
        large_mobile_production_units: an integer, the number of large mobile production units
        small_mobile_production_units: an integer, the number of small mobile production units
    Returns:
        obj: an integer, the total number of parking spots
    """
    obj = 0
    
    # Create a new model
    model = gp.Model("production_transportation")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of large mobile production units
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of small mobile production units
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(6*x + 2*y >= 80)
    model.addConstr(y >= 5)
    model.addConstr(x >= 0.75*(x + y))
    
    # Optimize the model
    model.optimize()
    
    # Get the total number of parking spots required
    obj = model.objVal
    
    return obj