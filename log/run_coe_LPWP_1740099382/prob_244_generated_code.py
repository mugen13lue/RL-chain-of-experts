import gurobipy as gp
from gurobipy import GRB

def prob_244(x, y, cut_limitation, waste_limitation):
    """
    Args:
        x: an integer, the number of chop saws
        y: an integer, the number of steel cutters
        cut_limitation: an integer, the cut limitation in pounds
        waste_limitation: an integer, the waste limitation in units
    Returns:
        obj: an integer, the objective value
    """
    model = gp.Model("metal_working_shop")

    # Decision variables
    chop_saw = model.addVar(vtype=GRB.INTEGER, name="chop_saw")
    steel_cutter = model.addVar(vtype=GRB.INTEGER, name="steel_cutter")

    # Constraints
    model.addConstr(25*chop_saw + 5*steel_cutter >= cut_limitation, "metal_cutting_constraint")
    model.addConstr(25*chop_saw + 3*steel_cutter <= waste_limitation, "waste_generation_constraint")

    # Objective
    model.setObjective(chop_saw + steel_cutter, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)