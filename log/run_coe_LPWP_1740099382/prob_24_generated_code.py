import gurobipy as gp
from gurobipy import GRB

def prob_24(large, small_art_pieces):
    """
    Args:
        large: an integer, indicating the number of large art pieces
        small_art_pieces: an integer, indicating the number of small art pieces
    Returns:
        obj: an integer, the objective value of the problem
    """
    
    # Create a new model
    model = gp.Model("art_store")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of large art pieces
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of small art pieces

    # Set objective function
    model.setObjective(30*x + 15*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(4*x + 2*y <= 100, "paint_constraint")
    model.addConstr(3*x + y <= 50, "glitter_constraint")
    model.addConstr(5*x + 2*y <= 70, "glue_constraint")
    model.addConstr(x >= 5, "min_large_constraint")
    model.addConstr(y >= 5, "min_small_constraint")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj