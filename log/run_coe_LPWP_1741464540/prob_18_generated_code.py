import gurobipy as gp
from gurobipy import GRB

def prob_18(Feed_A, Feed_B):
    """
    Args:
        Feed_A: an integer, representing the amount of Feed A
        Feed_B: an integer, representing the amount of Feed B
    Returns:
        obj: an integer, representing the minimum cost of the mixture
    """
    # Create a new model
    model = gp.Model("feed_mixture")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")

    # Set objective function
    model.setObjective(100*x + 80*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 7*y >= 30)
    model.addConstr(8*x + 15*y >= 50)

    # Optimize model
    model.optimize()

    # Get the minimum cost
    obj = model.objVal

    return obj