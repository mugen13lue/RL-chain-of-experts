import gurobipy as gp
from gurobipy import GRB

def prob_148(pill, shot):
    """
    Args:
        pill: an integer, the number of pill vaccines administered
        shot: an integer, the number of shot vaccines administered
    Returns:
        obj: an integer, the maximum number of patients vaccinated
    """
    model = gp.Model("vaccine_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="pill_vaccines")
    y = model.addVar(vtype=GRB.INTEGER, name="shot_vaccines")

    # Constraints
    model.addConstr(x >= 30, "min_pill_vaccines")
    model.addConstr(y >= 3*x, "min_shot_vaccines")
    model.addConstr(10*x + 20*y <= 10000, "total_time")

    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)