from gurobipy import *

def prob_56(wraps, platters, meat_wrap, rice_wrap, meat_platter, rice_platter, time_wrap, time_platter, wrap_to_platter_ratio): 
    """
    Args:
        wraps: an integer (number of wraps to produce)
        platters: an integer (number of platters to produce)
        meat_wrap: an integer (units of meat required for a wrap)
        rice_wrap: an integer (units of rice required for a wrap)
        meat_platter: an integer (units of meat required for a platter)
        rice_platter: an integer (units of rice required for a platter)
        time_wrap: an integer (time in minutes to produce a wrap)
        time_platter: an integer (time in minutes to produce a platter)
        wrap_to_platter_ratio: an integer (minimum ratio of wraps to platters)
        
    Returns:
        obj: a float (minimum total production time)
    """
    model = Model("production_optimization")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="wraps")
    y = model.addVar(vtype=GRB.INTEGER, name="platters")
    
    # Constraints
    model.addConstr(5*x + 7*y >= 3000, "Meat")
    model.addConstr(3*x + 5*y >= 2500, "Rice")
    model.addConstr(x >= wrap_to_platter_ratio*y, "Wraps_Platters_Ratio")
    
    # Objective
    model.setObjective(10*x + 8*y, GRB.MINIMIZE)
    
    # Optimize model
    model.optimize()
    
    return model.objVal