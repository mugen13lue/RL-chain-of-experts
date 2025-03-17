import gurobipy as gp
from gurobipy import GRB

def prob_169(camels, horses):
    """
    Args:
        camels: an integer indicating the number of camels
        horses: an integer indicating the number of horses
    Returns:
        obj: an integer, the minimal number of animals
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("animal_delivery")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="camels")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="horses")
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*x + 60*y >= 1000)
    model.addConstr(20*x + 30*y <= 450)
    model.addConstr(y <= x)
    
    # Optimize the model
    model.optimize()
    
    # Update the objective value
    obj = int(model.objVal)
    
    return obj