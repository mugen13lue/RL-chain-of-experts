import gurobipy as gp
from gurobipy import GRB

def prob_140(Beam_1, Beam_2):
    """
    Args:
        Beam_1: an integer, the number of minutes of Beam 1 used
        Beam_2: an integer, the number of minutes of Beam 2 used

    Returns:
        obj: an integer, the minimized total radiation received by the pancreas
    """
    model = gp.Model("radiation_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(0.3*x + 0.2*y <= 4, "Pancreas_Dose")
    model.addConstr(0.6*x + 0.4*y >= 3, "Tumor_Dose")

    # Objective
    model.setObjective(0.2*x + 0.1*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return the minimized total radiation received by the pancreas
    return int(model.objVal)