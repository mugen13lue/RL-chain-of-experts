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
    m = gp.Model("farm_optimization")
    
    # Define decision variables
    x = m.addVar(lb=12, vtype=GRB.CONTINUOUS, name="potatoes")
    y = m.addVar(lb=15, vtype=GRB.CONTINUOUS, name="cucumbers")
    
    # Set objective function
    m.setObjective(500*x + 650*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(y <= 2*x, "resource_constraint")
    m.addConstr(x + y <= 50, "total_acres_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the maximum profit
    obj = m.objVal
    
    return obj