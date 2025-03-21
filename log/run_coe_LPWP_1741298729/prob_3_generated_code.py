import gurobipy as gp
from gurobipy import GRB

def prob_3(apples, pears, constraint1, constraint2, constraint3, constraint4):
    """
    Args:
        apples: an integer - number of acres of apples to grow
        pears: an integer - number of acres of pears to grow
        constraint1: an integer - total available land in acres
        constraint2: an integer - minimum required acres of apples
        constraint3: an integer - minimum required acres of pears
        constraint4: a boolean - whether the pears should be at most twice the apples or not
    Returns:
        obj: an integer - optimal profit
    """
    
    # Create a new model
    m = gp.Model("fruit_optimization")
    
    # Decision variables
    x = m.addVar(lb=0, vtype=GRB.INTEGER, name="apples")
    y = m.addVar(lb=0, vtype=GRB.INTEGER, name="pears")
    
    # Objective function: Maximize profit
    m.setObjective(2*x + 4*y, sense=GRB.MAXIMIZE)
    
    # Constraints
    m.addConstr(x >= constraint2, "min_apple_acres")
    m.addConstr(y >= constraint3, "min_pear_acres")
    m.addConstr(x + y <= constraint1, "total_acres_constraint")
    
    if constraint4:
        m.addConstr(y <= 2*x, "pears_to_apples_ratio_constraint")
    
    # Optimize the model
    m.optimize()
    
    # Get the optimal profit
    obj = m.objVal
    
    return obj