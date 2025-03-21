import gurobipy as gp
from gurobipy import GRB

def prob_54(miter_saw, circular_saw, constraint1, constraint2):
    """
    Args:
        miter_saw: an integer, the number of miter saws to purchase
        circular_saw: an integer, the number of circular saws to purchase
        constraint1: an integer, the result of the first constraint
        constraint2: an integer, the result of the second constraint
    Returns:
        number_of_saws: an integer, the total number of saws needed
    """
    model = gp.Model("saw_purchase")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Objective function: minimize total number of saws
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(50*x >= constraint1, "min_planks_miter")
    model.addConstr(70*y >= constraint1, "min_planks_circular")
    model.addConstr(60*x <= constraint2, "max_sawdust_miter")
    model.addConstr(100*y <= constraint2, "max_sawdust_circular")

    model.optimize()

    number_of_saws = int(x.x) + int(y.x)

    return number_of_saws