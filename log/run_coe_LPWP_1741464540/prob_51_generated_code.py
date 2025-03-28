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

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of high intensity drills
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of low intensity drills

    # Constraints
    model.addConstr(50*x + 30*y >= 800, "gems_constraint")
    model.addConstr(50*x + 20*y <= 700, "water_constraint")
    model.addConstr(x <= 0.4*(x + y), "high_intensity_limit")
    model.addConstr(y >= 10, "low_intensity_limit")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)  # Minimum total number of drills needed