import gurobipy as gp
from gurobipy import GRB

def prob_215(constraint1, constraint2):
    """
    Args:
        constraint1: an integer representing the first constraint
        constraint2: an integer representing the second constraint

    Returns:
        obj: an integer representing the objective value
    """
    
    # Create a new model
    model = gp.Model("repairman_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="washing_machine")
    y = model.addVar(vtype=GRB.INTEGER, name="freezers")
    
    # Set objective function
    model.setObjective(250*x + 375*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 20*y <= constraint1, "inspection_constraint")
    model.addConstr(90*x + 125*y <= constraint2, "fixing_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj