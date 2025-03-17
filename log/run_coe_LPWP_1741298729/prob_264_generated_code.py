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

    # Define variables
    x = m.addVar(name="specialized_hours")
    y = m.addVar(name="common_hours")

    # Set objective
    m.setObjective(100*x + 72*y, sense=GRB.MINIMIZE)

    # Add constraints
    m.addConstr(x >= 0)
    m.addConstr(y >= 0)
    m.addConstr(x + y >= 333.33)
    m.addConstr(x + y >= 250)

    # Solve the optimization problem
    m.optimize()

    # Get the optimal cost
    obj = m.objVal

    return obj