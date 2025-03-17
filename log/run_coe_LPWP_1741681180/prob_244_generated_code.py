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
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="chop_saw")
    y = model.addVar(vtype=GRB.INTEGER, name="steel_cutter")
    
    # Parameters
    A = 25
    B = 5
    C = 25
    D = 3
    E = cut_limitation
    F = waste_limitation
    
    # Objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Constraints
    model.addConstr(A*x + B*y >= E, "cut_limitation")
    model.addConstr(C*x + D*y <= F, "waste_limitation")
    
    # Optimize the model
    model.optimize()
    
    # Return the objective value
    return int(model.objVal)