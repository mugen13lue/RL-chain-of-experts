from gurobipy import *

def prob_135(sulfate, ginger, constraint1, constraint2, constraint3):
    """
    Args:
        sulfate: an integer, the amount of sulfate to be added to the shampoo.
        ginger: an integer, the amount of ginger to be added to the shampoo.
        constraint1: a float, the amount of time it takes for one unit of sulfate to be effective.
        constraint2: a float, the amount of time it takes for one unit of ginger to be effective.
        constraint3: a string, the constraint on the ratio of sulfate to ginger.
    Returns:
        obj: the total amount of time it takes for the mixture to be effective.
    """
    m = Model("shampoo_optimization")
    
    # Decision variables
    x = m.addVar(lb=100, vtype=GRB.INTEGER, name="sulfate")
    y = m.addVar(lb=0, ub=400, vtype=GRB.INTEGER, name="ginger")
    
    # Objective function
    m.setObjective(constraint1 * x + constraint2 * y, GRB.MINIMIZE)
    
    # Constraints
    if constraint3 == "twice":
        m.addConstr(x <= 2 * y, "sulfate_ginger_ratio")
    
    m.addConstr(x + y == 400, "total_amount_constraint")
    
    # Optimize model
    m.optimize()
    
    return m.objVal