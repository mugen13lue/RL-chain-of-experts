import gurobipy as gp
from gurobipy import GRB

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
    model = gp.Model("production_optimization")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="wraps")
    y = model.addVar(vtype=GRB.INTEGER, name="platters")
    
    # Constraints
    model.addConstr(meat_wrap*x + meat_platter*y >= 3000, "meat_constraint")
    model.addConstr(rice_wrap*x + rice_platter*y >= 2500, "rice_constraint")
    model.addConstr(x >= wrap_to_platter_ratio*y, "wrap_platter_ratio_constraint")
    
    # Objective
    model.setObjective(time_wrap*x + time_platter*y, GRB.MINIMIZE)
    
    # Optimize model
    model.optimize()
    
    return model.objVal