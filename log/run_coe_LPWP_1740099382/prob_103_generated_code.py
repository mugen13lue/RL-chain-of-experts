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
    # Create a new model
    model = gp.Model("bone_production")

    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="small_bones")
    y = model.addVar(vtype=GRB.INTEGER, name="large_bones")
    M = model.addVar(vtype=GRB.CONTINUOUS, name="meat")

    # Set objective
    model.setObjective(M, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 15*y <= medication_constraint, "medication_constraint")
    model.addConstr(12*x <= M, "meat_for_small_bones")
    model.addConstr(15*y <= M, "meat_for_large_bones")
    model.addConstr(x >= 0.5*(x+y), "small_bones_percentage")
    model.addConstr(y >= minimum_large_bone_constraint, "minimum_large_bones")

    # Optimize model
    model.optimize()

    # Return the optimal values of small bones, large bones, and the amount of meat
    return int(x.x), int(y.x), int(M.x)