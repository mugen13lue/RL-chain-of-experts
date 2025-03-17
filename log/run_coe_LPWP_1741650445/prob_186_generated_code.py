import gurobipy as gp
from gurobipy import GRB

def prob_186(cows, elephants):
    """
    Args:
        cows: an integer, number of cows
        elephants: an integer, number of elephants
    Returns:
        obj: an integer, objective value
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("animal_transportation")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="cows")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="elephants")
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(20*x + 50*y >= 1000)
    model.addConstr(y <= x)
    model.addConstr(x <= 2*y)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj