import gurobipy as gp
from gurobipy import GRB

def prob_166(large_planes, small_planes):
    """
    Args:
        large_planes: an integer, the number of large planes
        small_planes: an integer, the number of small planes
    Returns:
        obj: an integer, the objective value
    """
    obj = 0

    # Create a new model
    model = gp.Model("plane_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x <= y)
    model.addConstr(30*x + 10*y >= 300)
    model.addConstr(x >= 0)
    model.addConstr(y >= 0)

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj