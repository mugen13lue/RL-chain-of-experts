import gurobipy as gp
from gurobipy import GRB

def prob_237(pop, rnb, constraint1, constraint2, constraint3):
    """
    Args:
        pop: an integer, number of pop concerts
        rnb: an integer, number of R&B concerts
        constraint1: an integer, constraint for total audience size
        constraint2: an integer, constraint for total practice days
        constraint3: a float, constraint for maximum percentage of R&B concerts
    Returns:
        obj: an integer, total number of concerts
    """
    
    # Create a new model
    model = gp.Model("concerts_optimization")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="pop_concerts")
    y = model.addVar(vtype=GRB.INTEGER, name="rnb_concerts")
    
    # Set objective function: minimize total number of concerts
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Constraints
    model.addConstr(100*x + 240*y >= constraint1, "audience_constraint")
    model.addConstr(2*x + 4*y <= constraint2, "practice_days_constraint")
    model.addConstr(y <= constraint3*(x + y), "rnb_limit_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the total number of concerts
    obj = model.objVal
    
    return obj