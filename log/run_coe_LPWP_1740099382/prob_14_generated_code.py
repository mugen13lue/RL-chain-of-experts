import gurobipy as gp
from gurobipy import GRB

def prob_14(long, short_cables, constraint1, constraint2, constraint3):
    """
    Args:
        long: an integer, the number of long cables
        short_cables: an integer, the number of short cables
        constraint1: an integer, the value of the first constraint
        constraint2: an integer, the value of the second constraint
        constraint3: an integer, the value of the third constraint

    Returns:
        obj: an integer, the objective value
    """
    # Create a new model
    model = gp.Model("cable_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="long_cables")
    y = model.addVar(vtype=GRB.INTEGER, name="short_cables")

    # Set objective function
    model.setObjective(12*x + 5*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(10*x + 7*y <= 1000, "gold_constraint")
    model.addConstr(y >= 5*x, "short_cable_constraint")
    model.addConstr(x >= 10, "long_cable_constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj