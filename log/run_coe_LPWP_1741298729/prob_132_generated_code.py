import gurobipy as gp
from gurobipy import GRB

def prob_132(table_1, table_2):
    """
    Args:
        table_1: an integer,
        table_2: an integer,
    Returns:
        obj: an integer,
    """
    # Create a new model
    model = gp.Model("slime_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(4*x + 5*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3*x + 8*y <= 100, "powder_constraint")
    model.addConstr(5*x + 6*y <= 90, "glue_constraint")
    model.addConstr(2*x + 4*y <= 30, "mess_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj