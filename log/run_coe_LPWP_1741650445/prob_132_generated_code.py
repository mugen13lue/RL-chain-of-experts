import gurobipy as gp
from gurobipy import GRB

def prob_132(table_1, table_2):
    """
    Args:
        table_1: an integer,
        table_2: an integer,
    Returns:
        obj: an integer,
    """
    model = gp.Model("slime_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(3*table_1 + 8*table_2 <= 100, "Powder")
    model.addConstr(5*table_1 + 6*table_2 <= 90, "Glue")
    model.addConstr(2*table_1 + 4*table_2 <= 30, "Mess")

    # Objective
    model.setObjective(4*table_1 + 5*table_2, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)