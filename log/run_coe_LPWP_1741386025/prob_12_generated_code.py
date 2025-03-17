import gurobipy as gp
from gurobipy import GRB

def prob_12(regular, special, constraint1, constraint2):
    """
    Args:
        regular: an integer, the number of regular sandwiches
        special: an integer, the number of special sandwiches
        constraint1: an integer, the first constraint value
        constraint2: an integer, the second constraint value
    Returns:
        obj: an integer, the objective value (profit)
    """
    # Create a new model
    model = gp.Model("sandwiches")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular")
    y = model.addVar(vtype=GRB.INTEGER, name="special")

    # Set objective function
    model.setObjective(3*x + 4*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 3*y <= constraint1, "eggs")
    model.addConstr(3*x + 5*y <= constraint2, "bacon")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj