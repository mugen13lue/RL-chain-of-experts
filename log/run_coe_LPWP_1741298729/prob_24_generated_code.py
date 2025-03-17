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
    m = gp.Model("art_store")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of large art pieces
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of small art pieces

    # Constraints
    m.addConstr(4*x + 2*y <= 100, "paint_constraint")
    m.addConstr(3*x + y <= 50, "glitter_constraint")
    m.addConstr(5*x + 2*y <= 70, "glue_constraint")
    m.addConstr(x >= 5, "min_large_constraint")
    m.addConstr(y >= 5, "min_small_constraint")

    # Objective
    m.setObjective(30*x + 15*y, GRB.MAXIMIZE)

    # Solve the model
    m.optimize()

    obj = m.objVal

    return obj