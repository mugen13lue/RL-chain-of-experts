import gurobipy as gp
from gurobipy import GRB

def prob_49():
    """
    Returns:
        obj: an integer, represents the objective value (revenue) to maximize
    """
    # Create a new model
    m = gp.Model("farm_optimization")
    
    # Decision variables
    x = m.addVar(lb=0, vtype=GRB.INTEGER, name="turnips")
    y = m.addVar(lb=0, vtype=GRB.INTEGER, name="pumpkins")
    
    # Set objective
    m.setObjective(300*x + 450*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(50*x + 90*y <= 40000, "watering_constraint")
    m.addConstr(80*x + 50*y <= 34000, "pesticide_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the objective value
    obj = m.objVal
    
    return obj