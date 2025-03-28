import gurobipy as gp
from gurobipy import GRB

def prob_24():
    # Create a new model
    model = gp.Model("art_store")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="large_art_pieces")
    x2 = model.addVar(vtype=GRB.INTEGER, name="small_art_pieces")

    # Objective function: maximize profit
    model.setObjective(30*x1 + 15*x2, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(4*x1 + 2*x2 <= 100, "paint_constraint")
    model.addConstr(3*x1 + x2 <= 50, "glitter_constraint")
    model.addConstr(5*x1 + 2*x2 <= 70, "glue_constraint")
    model.addConstr(x1 >= 5, "min_large_art_pieces")
    model.addConstr(x2 >= 5, "min_small_art_pieces")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj