import gurobipy as gp
from gurobipy import GRB

def prob_121(ramen, fries):
    """
    Args:
        ramen: an integer, the number of packs of ramen
        fries: an integer, the number of packs of fries
    Returns:
        obj: an integer, the value of the objective function
    """
    
    # Constants
    calories_ramen = 400
    protein_ramen = 20
    sodium_ramen = 100
    calories_fries = 300
    protein_fries = 10
    sodium_fries = 75
    
    # Create a new model
    model = gp.Model("salesman_diet")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="ramen")
    y = model.addVar(vtype=GRB.INTEGER, name="fries")
    
    # Set objective function: minimize sodium intake
    model.setObjective(100*x + 75*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(400*x + 300*y >= 3000, "calories_constraint")
    model.addConstr(20*x + 10*y >= 80, "protein_constraint")
    model.addConstr(100*x + 75*y <= gp.GRB.INFINITY, "sodium_constraint")
    model.addConstr(x <= 0.3*(x+y), "percentage_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj