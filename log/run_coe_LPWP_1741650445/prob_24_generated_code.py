import gurobipy as gp
from gurobipy import GRB

def prob_24():
    # Create a new model
    model = gp.Model("art_store")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of large art pieces
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of small art pieces

    # Set objective function
    model.setObjective(30*x + 15*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(4*x + 2*y <= 100, "Paint")
    model.addConstr(3*x + y <= 50, "Glitter")
    model.addConstr(5*x + 2*y <= 70, "Glue")
    model.addConstr(x >= 5, "Minimum Large Art Pieces")
    model.addConstr(y >= 5, "Minimum Small Art Pieces")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj