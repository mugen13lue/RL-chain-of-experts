import gurobipy as gp
from gurobipy import GRB

def prob_47(bagels, croissants, oven_hours, chef_hours):
    """
    Args:
        bagels: an integer, number of batches of bagels
        croissants: an integer, number of batches of croissants
        oven_hours: an integer, total oven hours used
        chef_hours: an integer, total chef hours used
    Returns:
        obj: an integer, maximum profit
    """
    # Create a new model
    model = gp.Model("bakery")

    # Decision variables
    num_bagels = model.addVar(vtype=GRB.INTEGER, name="num_bagels")
    num_croissants = model.addVar(vtype=GRB.INTEGER, name="num_croissants")

    # Set objective function
    model.setObjective(20*num_bagels + 40*num_croissants, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*num_bagels + num_croissants <= oven_hours, "oven_time")
    model.addConstr(0.25*num_bagels + 2*num_croissants <= chef_hours, "chef_time")
    model.addConstr(num_bagels >= 0, "non_negativity_bagels")
    model.addConstr(num_croissants >= 0, "non_negativity_croissants")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj