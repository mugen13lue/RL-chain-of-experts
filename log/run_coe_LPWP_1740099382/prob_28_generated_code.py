import gurobipy as gp
from gurobipy import GRB

def prob_28(phones, laptops):
    """
    Args:
        phones: an integer, number of phones
        laptops: an integer, number of laptops
    Returns:
        obj: an integer, maximum profit
    """
    # Create a new model
    model = gp.Model("inventory_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="phones")
    y = model.addVar(vtype=GRB.INTEGER, name="laptops")

    # Set objective function
    model.setObjective(120*x + 40*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(1*x + 4*y <= 400, "floor_space_constraint")
    model.addConstr(0.8*(x + y) <= y, "laptops_percentage_constraint")
    model.addConstr(400*x + 100*y <= 6000, "cost_constraint")

    # Optimize the model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj