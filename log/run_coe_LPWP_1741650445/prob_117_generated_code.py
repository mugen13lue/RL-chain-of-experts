import gurobipy as gp
from gurobipy import GRB

def prob_117(burgers, pizza):
    """
    Args:
        burgers: an integer, the number of burgers
        pizza: an integer, the number of pizza slices
    Returns:
        obj: an integer, the objective value (cholesterol intake)
    """
    model = gp.Model("diet_problem")
    
    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="burgers")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="pizza_slices")
    M = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="cholesterol_intake")
    
    # Set objective
    model.setObjective(M, GRB.MINIMIZE)
    
    # Constraints
    model.addConstr(10*x + 8*y >= 130, "fat_constraint")
    model.addConstr(300*x + 250*y >= 3000, "calories_constraint")
    model.addConstr(12*x + 10*y <= M, "cholesterol_constraint")
    model.addConstr(y >= 2*x, "pizza_burgers_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj