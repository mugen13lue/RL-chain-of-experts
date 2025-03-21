import gurobipy as gp
from gurobipy import GRB

def prob_253(small_boxes, large_boxes):
    """
    Solves the Box Packing problem.

    Args:
        small_boxes: an integer, representing the number of small boxes to be used.
        large_boxes: an integer, representing the number of large boxes to be used.

    Returns:
        obj: an integer, representing the objective value (minimize the total number of boxes needed).
    """
    model = gp.Model("Box_Packing")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(x >= 3*y, "Constraint1")
    model.addConstr(y >= 5, "Constraint2")
    model.addConstr(25*x + 45*y >= 750, "Constraint3")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)