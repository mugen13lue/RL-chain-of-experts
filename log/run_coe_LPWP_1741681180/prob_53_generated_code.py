import gurobipy as gp
from gurobipy import GRB

def prob_53(process_A, process_B):
    """
    Args:
        process_A: an integer,
        process_B: an integer,
    Returns:
        obj: an integer, 
    """
    # Create a new model
    model = gp.Model("coin_plating")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(process_A * x + process_B * y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3 * x + 5 * y <= 500, "gold_constraint")
    model.addConstr(2 * x + 3 * y <= 300, "wire_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj