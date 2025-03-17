import gurobipy as gp
from gurobipy import GRB

def prob_265(golf_carts, pull_carts):
    """
    Args:
        golf_carts: an integer, number of golf carts
        pull_carts: an integer, number of pull carts
    Returns:
        obj: an integer, the objective value
    """
    # Create a new model
    model = gp.Model("cart_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of golf carts
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of pull carts

    # Set objective function: minimize total number of carts
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(4*x + y >= 80, "guests_constraint")
    model.addConstr(x <= 0.6*(x + y), "golf_cart_limit")
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj