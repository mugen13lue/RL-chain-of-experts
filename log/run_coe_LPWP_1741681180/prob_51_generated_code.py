import gurobipy as gp
from gurobipy import GRB

def prob_51(high_intensity, low_intensity):
    """
    Args:
        high_intensity: an integer representing the number of high intensity drills
        low_intensity: an integer representing the number of low intensity drills

    Returns:
        obj: an integer, representing the minimum total number of drills needed
    """
    model = gp.Model("gem_factory")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="high_intensity_drills")
    y = model.addVar(vtype=GRB.INTEGER, name="low_intensity_drills")

    # Constraints
    model.addConstr(50*x + 30*y == 800, "gems_processed")
    model.addConstr(50*x + 20*y <= 700, "water_usage")
    model.addConstr(x <= 0.4*(x+y), "percentage_high_intensity")
    model.addConstr(y >= 10, "minimum_low_intensity")
    
    # Objective function
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    return int(model.objVal)