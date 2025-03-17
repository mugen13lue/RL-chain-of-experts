import gurobipy as gp
from gurobipy import GRB

def prob_108(regular_batch, premium_batch):
    """
    Args:
        regular_batch: an integer, number of regular batches
        premium_batch: an integer, number of premium batches
    Returns:
        obj: an integer, number of people treated
    """
    # Create a new model
    model = gp.Model("skin_cream_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_batches")
    y = model.addVar(vtype=GRB.INTEGER, name="premium_batches")

    # Set objective function
    model.setObjective(50*x + 30*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(50*x + 40*y <= 3000, "medicinal_ingredients")
    model.addConstr(40*x + 60*y <= 3500, "rehydration_product")
    model.addConstr(x >= 10, "regular_batches_minimum")
    model.addConstr(x <= y, "regular_batches_less_than_premium")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj