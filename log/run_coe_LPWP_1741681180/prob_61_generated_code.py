import gurobipy as gp
from gurobipy import GRB

def prob_61(new_model, old_model):
    """
    Args:
        new_model: an integer, the number of new model furnaces
        old_model: an integer, the number of old model furnaces

    Returns:
        obj: a float, the objective value
    """
    m = gp.Model("furnace_purchase")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="new_model")
    y = m.addVar(vtype=GRB.INTEGER, name="old_model")

    # Objective function: minimize the total number of furnaces
    m.setObjective(x + y, GRB.MINIMIZE)

    # Constraints
    m.addConstr(10*x + 15*y >= 200, "heating_constraint")
    m.addConstr(200*x + 250*y <= 3500, "electricity_constraint")
    m.addConstr(y <= 0.35*(x+y), "old_model_limit")
    m.addConstr(x >= 5, "new_model_limit")

    m.optimize()

    obj = m.objVal

    return obj