import gurobipy as gp
from gurobipy import GRB

def prob_139(spit_tests, swabs):
    """
    Args:
        spit_tests: an integer, the number of spit tests
        swabs: an integer, the number of swabs
    Returns:
        obj: an integer, the objective value
    """
    obj = 0
    
    # Create a new model
    model = gp.Model("virus_testing")
    
    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="spit_tests")
    y = model.addVar(vtype=GRB.INTEGER, name="swabs")
    
    # Set objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(x >= 2*y)
    model.addConstr(y >= 20)
    model.addConstr(10*x + 15*y <= 8000)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj