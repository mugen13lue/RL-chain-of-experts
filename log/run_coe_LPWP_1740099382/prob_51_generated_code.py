import gurobipy as gp
from gurobipy import GRB

def prob_51():
    """
    Returns:
        obj: an integer, representing the minimum total number of drills needed
    """
    # Create a new model
    model = gp.Model("gem_factory")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of high intensity drills
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of low intensity drills

    # Set objective function: minimize total number of drills
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 30*y >= 800)
    model.addConstr(50*x + 20*y <= 700)
    model.addConstr(x <= 0.4*(x+y))
    model.addConstr(y >= 10)

    # Optimize the model
    model.optimize()

    # Get the minimum total number of drills needed
    obj = model.objVal

    return obj