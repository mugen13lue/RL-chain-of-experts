import gurobipy as gp
from gurobipy import GRB

def prob_209():
    """
    Returns:
        obj: an integer representing the minimum cost
        regular_brand: an integer representing the number of bags of regular brand
        premium_brand: an integer representing the number of bags of premium brand
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("dog_food_mixing")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_brand")
    y = model.addVar(vtype=GRB.INTEGER, name="premium_brand")
    
    # Set objective function: Minimize Cost
    model.setObjective(20*x + 35*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(4*x + 12*y >= 15)
    model.addConstr(7*x + 10*y >= 20)
    model.addConstr(10*x + 16*y >= 20)
    
    # Optimize the model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        obj = model.objVal
        regular_brand = x.x
        premium_brand = y.x
    
    return obj, regular_brand, premium_brand