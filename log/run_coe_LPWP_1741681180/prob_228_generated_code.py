import gurobipy as gp
from gurobipy import GRB

def prob_228(densely_seated_one, loosely_seated_one):
    """
    Solve the ski lifts problem to minimize the total number of ski lifts needed.

    Args:
        densely_seated_one: Number of densely-seated ski lifts (integer).
        loosely_seated_one: Number of loosely-seated ski lifts (integer).

    Returns:
        total_lifts: Total number of ski lifts needed (integer).
    """
    model = gp.Model("ski_lifts")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="densely_seated_lifts")
    x2 = model.addVar(vtype=GRB.INTEGER, name="loosely_seated_lifts")

    # Objective function: minimize total number of ski lifts
    model.setObjective(x1 + x2, GRB.MINIMIZE)

    # Constraints
    model.addConstr(45*x1 + 20*x2 >= 1000, "guests_constraint")
    model.addConstr(30*x1 + 22*x2 <= 940, "electricity_constraint")
    model.addConstr(x2 >= loosely_seated_one, "minimum_loosely_seated_lifts")

    # Optimize model
    model.optimize()

    total_lifts = model.objVal

    return total_lifts