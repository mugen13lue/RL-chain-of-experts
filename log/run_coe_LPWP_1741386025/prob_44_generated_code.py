import gurobipy as gp
from gurobipy import GRB

def prob_44(scooters, bikes, constraint1, constraint2):
    """
    Args:
        scooters: an integer, representing the number of scooters
        bikes: an integer, representing the number of bikes
        constraint1: an integer, representing the value of the first constraint
        constraint2: an integer, representing the value of the second constraint
    Returns:
        obj: an integer, representing the objective value
    """
    
    # Create a new model
    model = gp.Model("profit_maximization")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="scooters")
    y = model.addVar(vtype=GRB.INTEGER, name="bikes")
    
    # Set objective function
    model.setObjective(200*x + 300*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(2*x + 4*y <= constraint1, "design_team_constraint")
    model.addConstr(3*x + 5*y <= constraint2, "engineering_team_constraint")
    model.addConstr(x >= 0, "non_negativity_constraint_scooters")
    model.addConstr(y >= 0, "non_negativity_constraint_bikes")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj