import gurobipy as gp
from gurobipy import GRB

def prob_173(van, minibus):
    """
    Args:
        van: an integer, represents the number of vans used
        minibus: an integer, represents the number of minibuses used
    Returns:
        obj: an integer, the total amount of pollution produced
    """
    # Create a new model
    model = gp.Model("transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of vans used
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of minibuses used

    # Set objective function
    model.setObjective(7*x + 10*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(6*x + 10*y >= 150, "num_kids_constraint")
    model.addConstr(y <= 10, "num_minibuses_constraint")
    model.addConstr(x >= y, "num_vans_constraint")

    # Optimize model
    model.optimize()

    # Get the total amount of pollution produced
    obj = model.objVal

    return obj