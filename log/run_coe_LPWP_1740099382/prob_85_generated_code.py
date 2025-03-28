import gurobipy as gp
from gurobipy import GRB

def prob_85(net_acres, fishing_line_acres, sum_in_a, linear_available, linear_at_most): 
    """
    Args:
        net_acres: an integer, representing the number of acres to use the net.
        fishing_line_acres: an integer, representing the number of acres to use the fishing line.
        sum_in_a: an integer, representing the sum of acres in the lake.
        linear_available: an integer, representing the available units of bait.
        linear_at_most: an integer, representing the maximum units of pain the fisherman can tolerate.

    Returns:
        obj: an integer, representing the maximum amount of fish the fisherman can catch.
    """
    
    # Create a new model
    model = gp.Model("fishing_problem")
    
    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="net_acres")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="fishing_line_acres")
    
    # Set objective
    model.setObjective(8*x + 5*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(8*x + 5*y <= sum_in_a, "fish_constraint")
    model.addConstr(4*x + 3*y <= linear_available, "bait_constraint")
    model.addConstr(2*x + y <= linear_at_most, "pain_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj