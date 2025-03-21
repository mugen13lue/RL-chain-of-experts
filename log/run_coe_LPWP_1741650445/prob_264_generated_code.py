import gurobipy as gp
from gurobipy import GRB

def prob_264(specialized_third_party, common_third_party_annotation_company):
    """
    Args:
        specialized_third_party: an integer, the number of images annotated by the specialized third-party company
        common_third_party_annotation_company: an integer, the number of images annotated by the common third-party annotation company
    Returns:
        obj: an integer, the cost of annotating the whole dataset
    """
    m = gp.Model("annotation_optimization")

    # Variables
    x = m.addVar(name="specialized_hours")
    y = m.addVar(name="common_hours")

    # Constraints
    m.addConstr(x + y >= 250, "total_hours_constraint")
    m.addConstr(x >= 83, "specialized_constraint")

    # Objective
    m.setObjective(100*x + 72*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Get the cost of annotating the whole dataset
    obj = m.objVal

    return obj