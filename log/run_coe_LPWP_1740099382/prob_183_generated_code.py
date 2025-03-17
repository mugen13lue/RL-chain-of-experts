import gurobipy as gp
from gurobipy import GRB

def prob_183(hot_air_balloon, gondola_lift):
    """
    Args:
        hot_air_balloon: an integer, represents the maximum number of hot air balloons rides
        gondola_lift: an integer, represents the maximum number of gondola lift rides
    Returns:
        obj: an integer, the minimized total pollution produced
    """
    
    # Create a new model
    model = gp.Model("transport_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of hot air balloon rides
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of gondola lift rides
    
    # Set objective function: minimize total pollution produced
    model.setObjective(10*x + 15*y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(4*x + 6*y >= 70, "total_visitors_constraint")
    model.addConstr(x <= hot_air_balloon, "max_hot_air_balloon_rides_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the minimized total pollution produced
    obj = model.objVal
    
    return obj