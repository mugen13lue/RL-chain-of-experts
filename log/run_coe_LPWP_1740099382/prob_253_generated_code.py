import gurobipy as gp
from gurobipy import GRB

def prob_253():
    """
    Solves the Box Packing problem.

    Returns:
        obj: an integer, representing the objective value (minimize the total number of boxes needed).
    """
    # Create a new model
    model = gp.Model("box_packing")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # number of small boxes
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # number of large boxes

    # Set objective function: minimize total number of boxes
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x >= 3*y, "constraint1")
    model.addConstr(25*x + 45*y >= 750, "constraint2")
    model.addConstr(y >= 5, "constraint3")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj