import gurobipy as gp
from gurobipy import GRB

def prob_281(coconut_oil, lavender):
    """
    Args:
        coconut_oil: an integer, the number of units of coconut oil to be added
        lavender: an integer, the number of units of lavender to be added
    Returns:
        obj: an integer, the total amount of time
    """
    # Create a new model
    model = gp.Model("body_wash_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="coconut_oil")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="lavender")

    # Set objective function
    model.setObjective(0.7*x + 0.9*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(0.7*x + 0.9*y >= 300)
    model.addConstr(0.7*x + 0.9*y <= 550)
    model.addConstr(x <= 3*y)

    # Optimize the model
    model.optimize()

    # Get the total amount of time
    obj = model.objVal

    return obj