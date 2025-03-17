import gurobipy as gp
from gurobipy import GRB

def prob_92(medium_sized_factory, small_factory):
    """
    Args:
        medium_sized_factory: an integer, the number of medium-sized factories
        small_factory: an integer, the number of small factories

    Returns:
        obj: an integer, the objective value
    """
    # Create a new model
    model = gp.Model("toy_factory")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of medium sized factories
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of small factories

    # Set objective function: minimize the total number of factories
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 35*y >= 250, "toy_production")
    model.addConstr(3*x + 2*y <= 16, "operator_constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj