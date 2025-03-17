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
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of miter saws
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of circular saws

    # Constraints
    model.addConstr(50*x + 70*y >= constraint1, "planks_constraint")
    model.addConstr(60*x + 100*y <= constraint2, "sawdust_constraint")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    number_of_saws = model.objVal

    return number_of_saws