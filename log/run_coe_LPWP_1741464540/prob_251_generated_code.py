import gurobipy as gp
from gurobipy import GRB

def prob_251(freight, air):
    """
    Args:
        freight: an integer, number of trips by freight
        air: an integer, number of trips by air
    Returns:
        obj: an integer, total number of trips
    """
    m = gp.Model("transportation_problem")
    
    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="freight")
    y = m.addVar(vtype=GRB.INTEGER, name="air")
    
    # Constraints
    m.addConstr(5*x + 3*y >= 200, "transportation_constraint")
    m.addConstr(300*x + 550*y <= 20000, "budget_constraint")
    m.addConstr(y >= 0.3*(x+y), "air_transportation_constraint")
    m.addConstr(x >= 5, "minimum_trips_by_freight_constraint")
    
    # Objective
    m.setObjective(x + y, GRB.MINIMIZE)
    
    # Optimize model
    m.optimize()
    
    obj = m.objVal
    
    return obj