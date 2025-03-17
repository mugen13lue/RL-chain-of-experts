import gurobipy as gp
from gurobipy import GRB

def prob_190(small_crates, large_crates):
    """
    Args:
        small_crates: an integer (number of small crates),
        large_crates: an integer (number of large crates)

    Returns:
        obj: an integer (total number of grapes)
    """
    # Create a new model
    model = gp.Model("grape_transport")

    # Define decision variables
    x = model.addVar(lb=0, ub=100, vtype=GRB.INTEGER, name="small_crates")
    y = model.addVar(lb=10, ub=50, vtype=GRB.INTEGER, name="large_crates")

    # Set objective function
    model.setObjective(200*x + 500*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x >= 3*y, "constraint1")
    model.addConstr(x + y <= 60, "constraint2")

    # Optimize model
    model.optimize()

    # Get the total number of grapes
    obj = int(model.objVal)

    return obj