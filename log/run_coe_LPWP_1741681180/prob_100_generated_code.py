import gurobipy as gp
from gurobipy import GRB

def prob_100(Pill_1, Pill_2):
    """
    Args:
        Pill_1: an integer, the number of Pill 1 taken
        Pill_2: an integer, the number of Pill 2 taken
    Returns:
        obj: an integer, the total amount of discharge
    """
    model = gp.Model("pill_optimization")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Objective function
    model.setObjective(0.3*x + 0.1*y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(0.2*x + 0.6*y <= 6, "pain_medication_constraint")
    model.addConstr(0.3*x + 0.2*y >= 3, "anxiety_medication_constraint")

    # Optimize model
    model.optimize()

    # Get the total amount of discharge
    obj = model.objVal

    return obj