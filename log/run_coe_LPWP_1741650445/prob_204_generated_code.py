import gurobipy as gp
from gurobipy import GRB

def prob_204(milk, vegetables):
    """
    Args:
        milk: an integer, amount of milk
        vegetables: an integer, amount of vegetables
    Returns:
        obj: an integer, objective value (cost)
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="milk")
    y = model.addVar(vtype=GRB.INTEGER, name="vegetables")

    # Set objective
    model.setObjective(x + 2*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(40*x + 15*y >= 100)
    model.addConstr(25*x + 30*y >= 50)

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj