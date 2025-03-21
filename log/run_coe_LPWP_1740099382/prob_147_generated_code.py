import gurobipy as gp
from gurobipy import GRB

def prob_147():
    """
    Returns:
        obj: an integer, representing the maximum total mass that can be supported
    """
    model = gp.Model("Bridge_Building")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="beam_bridges")
    y = model.addVar(vtype=GRB.INTEGER, name="truss_bridges")

    # Constraints
    model.addConstr(30*x + 50*y <= 600, "popsicle_sticks_constraint")
    model.addConstr(5*x + 8*y <= 100, "glue_constraint")
    model.addConstr(y <= 5, "truss_bridges_limit_constraint")
    model.addConstr(x >= y, "beam_bridges_more_than_truss_constraint")

    # Objective
    model.setObjective(40*x + 60*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)