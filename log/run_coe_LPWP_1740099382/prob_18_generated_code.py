import gurobipy as gp
from gurobipy import GRB

def prob_18():
    """
    Returns:
        obj: an integer, representing the minimum cost of the mixture
    """
    # Create a new LP model
    model = gp.Model("feed_mixing")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # amount of Feed A
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # amount of Feed B

    # Set objective function: minimize cost
    model.setObjective(100*x + 80*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 7*y >= 30, "Protein")
    model.addConstr(8*x + 15*y >= 50, "Fat")

    # Optimize model
    model.optimize()

    # Get the minimum cost of the mixture
    obj = model.objVal

    return obj