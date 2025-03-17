import gurobipy as gp
from gurobipy import GRB

def prob_252(large_mobile_production_units, small_mobile_production_units):
    """
    Args:
        large_mobile_production_units: an integer, the number of large mobile production units
        small_mobile_production_units: an integer, the number of small mobile production units
    Returns:
        obj: an integer, the total number of parking spots
    """
    total_people = 80
    min_small_units = 5
    min_large_units = total_people - min_small_units * 2
    min_large_percentage = 0.75
    
    m = gp.Model("production_transportation")
    
    large_units = m.addVar(vtype=GRB.INTEGER, name="large_units")
    small_units = m.addVar(vtype=GRB.INTEGER, name="small_units")
    
    m.addConstr(large_units >= min_large_units)
    m.addConstr(small_units >= min_small_units)
    m.addConstr(large_units >= total_people * min_large_percentage)
    
    m.setObjective(2 * large_units + small_units, sense=GRB.MINIMIZE)
    
    m.optimize()
    
    total_parking_spots = m.objVal
    
    return total_parking_spots