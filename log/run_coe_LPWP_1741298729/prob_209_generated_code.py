import gurobipy as gp
from gurobipy import GRB

def prob_209():
    """
    Returns:
        obj: an integer representing the minimum cost
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("dog_food_mixing")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_bags")
    y = model.addVar(vtype=GRB.INTEGER, name="premium_bags")
    
    # Set objective function: minimize cost
    model.setObjective(20*x + 35*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(4*x + 12*y >= 15, "calcium_constraint")
    model.addConstr(7*x + 10*y >= 20, "vitamin_constraint")
    model.addConstr(10*x + 16*y >= 20, "protein_constraint")
    
    # Optimize model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        obj = model.objVal
    
    return obj