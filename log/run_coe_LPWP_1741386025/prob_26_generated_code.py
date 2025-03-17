from gurobipy import *

def prob_26(Zodiac, Sunny):
    """
    Args:
        Zodiac: an integer, number of pills of Zodiac
        Sunny: an integer, number of pills of Sunny
    Returns:
        obj: an integer, objective value
    """
    
    # Create a new model
    m = Model("Medicine Optimization")
    
    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="Zodiac")
    y = m.addVar(vtype=GRB.INTEGER, name="Sunny")
    
    # Objective function: Minimize Cost = x + 3y
    m.setObjective(x + 3*y, GRB.MINIMIZE)
    
    # Constraints
    m.addConstr(1.3*x + 1.2*y >= 5, "Z1 Requirement")
    m.addConstr(1.5*x + 5*y >= 10, "D3 Requirement")
    
    # Optimize the model
    m.optimize()
    
    # Get the objective value
    obj = m.objVal
    
    return obj