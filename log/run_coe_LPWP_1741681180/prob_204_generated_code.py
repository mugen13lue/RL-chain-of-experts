import gurobipy as gp
from gurobipy import GRB

def prob_204():
    """
    Returns:
        obj: an integer, objective value (cost)
    """
    # Create a new model
    model = gp.Model("minimize_cost")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="milk")
    y = model.addVar(vtype=GRB.INTEGER, name="vegetables")

    # Set objective function: Minimize Cost
    model.setObjective(x + 2*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(40*x + 15*y >= 100, "calcium")
    model.addConstr(25*x + 30*y >= 50, "iron")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj