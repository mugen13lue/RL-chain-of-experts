import gurobipy as gp
from gurobipy import GRB

def prob_40(potatoes, cucumbers):
    """
    Args:
        potatoes: an integer, representing the number of acres of potatoes grown
        cucumbers: an integer, representing the number of acres of cucumbers grown
        
    Returns:
        obj: an integer, representing the maximum profit
    """
    
    # Create a new model
    model = gp.Model("farm_optimization")
    
    # Define decision variables
    x = model.addVar(lb=12, vtype=GRB.CONTINUOUS, name="potatoes")
    y = model.addVar(lb=15, vtype=GRB.CONTINUOUS, name="cucumbers")
    
    # Set objective function
    model.setObjective(500*x + 650*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(x + y <= 50, "resource_constraint")
    model.addConstr(y <= 2*x, "cucumber_limit")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj