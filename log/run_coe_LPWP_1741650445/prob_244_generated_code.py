import gurobipy as gp
from gurobipy import GRB

def prob_244(chop_saw, steel_cutter, cut_limitation, waste_limitation):
    """
    Args:
        chop_saw: an integer, the number of chop saws
        steel_cutter: an integer, the number of steel cutters
        cut_limitation: an integer, the cut limitation in pounds
        waste_limitation: an integer, the waste limitation in units
    Returns:
        obj: an integer, the objective value
    """
    
    # Create a new model
    model = gp.Model("metal_working_shop")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="chop_saw")
    y = model.addVar(vtype=GRB.INTEGER, name="steel_cutter")

    # Set objective function: minimize the total number of metal-working equipment needed
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(25*x + 5*y >= cut_limitation, "metal_cutting_constraint")
    model.addConstr(25*x + 3*y <= waste_limitation, "waste_generation_constraint")
    model.addConstr(x >= 0, "non_negativity_constraint_x")
    model.addConstr(y >= 0, "non_negativity_constraint_y")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj