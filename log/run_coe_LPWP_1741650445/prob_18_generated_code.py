import gurobipy as gp
from gurobipy import GRB

def prob_18():
    """
    Returns:
        obj: an integer, representing the minimum cost of the mixture
    """
    # Create a new model
    model = gp.Model("Feed_Mixture")

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

    # Get the minimum cost of the mixture
    obj = model.objVal

    return obj