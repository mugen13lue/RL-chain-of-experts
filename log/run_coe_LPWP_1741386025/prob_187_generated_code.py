import gurobipy as gp
from gurobipy import GRB

def prob_187(ferry, light_rail, constraint1, constraint2, constraint3):
    """
    Args:
        ferry: an integer, the number of ferry trips
        light_rail: an integer, the number of light rail trips
        constraint1: an integer, the first constraint parameter
        constraint2: an integer, the second constraint parameter
        constraint3: an integer, the third constraint parameter
    Returns:
        obj: an integer, the objective value
    """
    
    # Create a new model
    model = gp.Model("transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of ferry trips
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of light rail trips

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x >= 0, name="constraint1")
    model.addConstr(y >= 0, name="constraint2")
    model.addConstr(20*x + 15*y >= 500, name="constraint3")
    model.addConstr(y >= 4*x, name="constraint4")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj