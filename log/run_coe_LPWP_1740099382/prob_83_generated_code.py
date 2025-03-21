import gurobipy as gp
from gurobipy import GRB

def prob_83(var_4wheeler, var_3wheeler):
    """
    Args:
        var_4wheeler: an integer, number of 4-wheeler vehicles
        var_3wheeler: an integer, number of 3-wheeler vehicles
    Returns:
        obj: an integer, objective value
    """
    obj = 0
    
    # Create a new model
    model = gp.Model("vehicle_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of 4-wheeler vehicles
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of 3-wheeler vehicles
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(60*x + 40*y >= 1000, "luggage_constraint")
    model.addConstr(30*x + 15*y <= 430, "pollutant_constraint")
    
    # Optimize the model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        obj = model.objVal
        var_4wheeler = x.x
        var_3wheeler = y.x
    
    return obj