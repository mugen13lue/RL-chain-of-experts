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
    num_pill_vaccines = model.addVar(vtype=GRB.INTEGER, name="pill_vaccines")
    num_shot_vaccines = model.addVar(vtype=GRB.INTEGER, name="shot_vaccines")

    # Constraints
    model.addConstr(10*num_pill_vaccines + 20*num_shot_vaccines <= 10000, "administering_time_constraint")
    model.addConstr(num_shot_vaccines >= 3*num_pill_vaccines, "minimum_shot_vaccines_constraint")
    model.addConstr(num_pill_vaccines >= 30, "minimum_pill_vaccines_constraint")

    # Objective
    model.setObjective(num_pill_vaccines + num_shot_vaccines, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    obj = int(model.objVal)

    return obj