import gurobipy as gp
from gurobipy import GRB

def prob_107(fish, chicken):
    """
    Args:
        fish: an integer, number of fish meals
        chicken: an integer, number of chicken meals
    Returns:
        obj: an integer, minimized fat intake
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="fish")
    y = model.addVar(vtype=GRB.INTEGER, name="chicken")
    F = model.addVar(vtype=GRB.INTEGER, name="fat")

    # Set objective function
    model.setObjective(F, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 15*y >= 130)
    model.addConstr(12*x + 8*y >= 120)
    model.addConstr(7*x + 10*y == F)

    # Optimize the model
    model.optimize()

    # Get the minimized fat intake
    obj = model.objVal

    return int(obj)  # Return as integer