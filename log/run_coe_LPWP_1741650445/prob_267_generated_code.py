import gurobipy as gp
from gurobipy import GRB

def prob_267(basketballs, footballs):
    """
    Args:
        basketballs: an integer, representing the number of basketballs
        footballs: an integer, representing the number of footballs
        
    Returns:
        obj: an integer, representing the total number of sports equipment produced
    """
    
    # Create a new model
    model = gp.Model("sports_equipment_production")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="basketballs")
    y = model.addVar(vtype=GRB.INTEGER, name="footballs")
    
    # Set objective function
    model.setObjective(3*x + y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 3*y <= 1500, "materials_constraint")
    model.addConstr(x + 2*y <= 750, "labor_constraint")
    model.addConstr(x >= 3*y, "minimum_basketballs_constraint")
    model.addConstr(y >= 50, "minimum_footballs_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the total number of sports equipment produced
    obj = model.objVal
    
    return obj