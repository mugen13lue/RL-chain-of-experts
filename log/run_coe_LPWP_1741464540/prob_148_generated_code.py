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
    model = gp.Model("vaccine_administration")

    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="pill_vaccines")
    y = model.addVar(vtype=GRB.INTEGER, name="shot_vaccines")

    # Set objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x >= 30)
    model.addConstr(y >= 3*x)
    model.addConstr(10*x + 20*y <= 10000)

    # Optimize model
    model.optimize()

    # Get the maximum number of patients vaccinated
    obj = int(model.objVal)

    return obj