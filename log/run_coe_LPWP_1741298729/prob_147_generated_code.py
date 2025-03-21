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
    model = gp.Model("bridge_building")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="beam_bridges")
    y = model.addVar(vtype=GRB.INTEGER, name="truss_bridges")

    # Constraints
    model.addConstr(30*x + 50*y <= 600)
    model.addConstr(5*x + 8*y <= 100)
    model.addConstr(y <= 5)
    model.addConstr(x >= y)

    # Objective
    model.setObjective(40*x + 60*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)