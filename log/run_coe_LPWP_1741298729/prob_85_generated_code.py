import gurobipy as gp
from gurobipy import GRB

def prob_85(net, fishing_line, sum_in_a, linear_available, linear_at_most): 
    """
    Args:
        net: an integer, representing the number of acres to use the net.
        fishing_line: an integer, representing the number of acres to use the fishing line.
        sum_in_a: an integer, representing the sum of acres in the lake.
        linear_available: an integer, representing the available units of bait.
        linear_at_most: an integer, representing the maximum units of pain the fisherman can tolerate.

    Returns:
        obj: an integer, representing the maximum amount of fish the fisherman can catch.
    """
    obj = 0
    
    # Create a new model
    model = gp.Model("fishing_problem")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="net_acres")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="fishing_line_acres")
    
    # Set objective function
    model.setObjective(8*x + 5*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(4*x + 3*y <= linear_available, "bait_constraint")
    model.addConstr(2*x + y <= linear_at_most, "pain_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj