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
    obj = 0
    
    # Create a new model
    model = gp.Model("hay_processing")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # acres processed by windrower
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # acres processed by hay harvester
    
    # Set objective function
    model.setObjective(10*x + 8*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(10*x + 8*y <= 200, "hay_processing_constraint")
    model.addConstr(5*x + 3*y <= 800, "methane_gas_production_constraint")
    model.addConstr(2*x + y <= 300, "fuel_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj