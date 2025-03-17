import gurobipy as gp
from gurobipy import GRB

def prob_103(small_bone, large_bone, medication_constraint, small_bone_percentage_constraint, minimum_large_bone_constraint):
    """
    Args:
        small_bone: an integer.
        large_bone: an integer.
        medication_constraint: an integer.
        small_bone_percentage_constraint: an integer.
        minimum_large_bone_constraint: an integer.
    Returns:
        amount_of_meat: an integer.
    """
    model = gp.Model("bone_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="small_bones")
    y = model.addVar(vtype=GRB.INTEGER, name="large_bones")
    M = model.addVar(vtype=GRB.INTEGER, name="meat")

    # Constraints
    model.addConstr(10*x + 15*y <= medication_constraint, "tooth_medication")
    model.addConstr(12*x <= M, "meat_small_bones")
    model.addConstr(15*y <= M, "meat_large_bones")
    model.addConstr(x >= 0.5*(x+y), "min_small_bones")
    model.addConstr(y >= minimum_large_bone_constraint, "min_large_bones")

    # Objective
    model.setObjective(M, GRB.MINIMIZE)

    model.optimize()

    amount_of_meat = model.objVal

    return amount_of_meat