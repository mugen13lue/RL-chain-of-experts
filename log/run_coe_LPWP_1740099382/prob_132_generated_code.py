import gurobipy as gp
from gurobipy import GRB

def prob_132():
    """
    Returns:
        x: an integer, number of tables set up at table 1,
        y: an integer, number of tables set up at table 2
    """
    model = gp.Model("slime_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(3*x + 8*y <= 100, "powder_constraint")
    model.addConstr(5*x + 6*y <= 90, "glue_constraint")
    model.addConstr(2*x + 4*y <= 30, "mess_constraint")

    # Objective
    model.setObjective(4*x + 5*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(x.x), int(y.x)