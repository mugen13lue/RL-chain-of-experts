import gurobipy as gp
from gurobipy import GRB

def prob_24():
    # Create a new model
    model = gp.Model("art_store")
    
    # Create variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of large art pieces
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of small art pieces
    
    # Set objective function
    model.setObjective(30*x + 15*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(4*x + 2*y <= 100, "paint_constraint")
    model.addConstr(3*x + y <= 50, "glitter_constraint")
    model.addConstr(5*x + 2*y <= 70, "glue_constraint")
    model.addConstr(x >= 5, "min_large_art_pieces")
    model.addConstr(y >= 5, "min_small_art_pieces")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj