import gurobipy as gp
from gurobipy import GRB

def prob_169():
    """
    Returns:
        obj: an integer, the minimal number of animals
    """
    # Create a new model
    model = gp.Model("animal_delivery")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="camels")
    y = model.addVar(vtype=GRB.INTEGER, name="horses")

    # Set objective function: minimize total number of animals
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 60*y >= 1000, "packages")
    model.addConstr(20*x + 30*y <= 450, "food")
    model.addConstr(y <= x, "horses")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj