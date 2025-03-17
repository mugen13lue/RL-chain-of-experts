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
    obj = 1e9
    
    # Create a new model
    model = gp.Model("vehicle_optimization")
    
    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="4wheeler")
    x2 = model.addVar(vtype=GRB.INTEGER, name="3wheeler")
    
    # Set objective
    model.setObjective(x1 + x2, GRB.MINIMIZE)
    
    # Constraints
    model.addConstr(60*x1 + 40*x2 >= 1000)
    model.addConstr(30*x1 + 15*x2 <= 430)
    
    # Optimize the model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        obj = model.objVal
    
    return obj