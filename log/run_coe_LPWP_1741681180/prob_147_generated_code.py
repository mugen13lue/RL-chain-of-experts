import gurobipy as gp
from gurobipy import GRB

def prob_147(beam_bridges, truss_bridges):
    """
    Args:
        beam_bridges: an integer, representing the number of beam bridges
        truss_bridges: an integer, representing the number of truss bridges
        
    Returns:
        obj: an integer, representing the maximum total mass that can be supported
    """
    
    # Create a new model
    model = gp.Model("bridge_building")
    
    # Decision variables
    beam = model.addVar(vtype=GRB.INTEGER, name="beam")
    truss = model.addVar(vtype=GRB.INTEGER, name="truss")
    
    # Objective function: maximize total mass
    model.setObjective(40*beam + 60*truss, sense=GRB.MAXIMIZE)
    
    # Constraints
    model.addConstr(30*beam + 50*truss <= 600, "sticks_constraint")
    model.addConstr(5*beam + 8*truss <= 100, "glue_constraint")
    model.addConstr(truss <= 5, "truss_limit")
    model.addConstr(beam > truss, "beam_greater_than_truss")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = int(model.objVal)
    
    return obj