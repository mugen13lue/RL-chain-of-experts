from gurobipy import *

def prob_36(Oil_Max, Oil_Max_Pro, Constraint_A, Constraint_B, Constraint_C):
    """
    Args:
        Oil_Max: an integer, number of containers of Oil Max
        Oil_Max_Pro: an integer, number of containers of Oil Max Pro
        Constraint_A: an integer, value of constraint A
        Constraint_B: an integer, value of constraint B
        Constraint_C: an integer, value of constraint C

    Returns:
        Profit: an integer, maximum profit
    """
    m = Model()

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="Oil_Max")
    y = m.addVar(vtype=GRB.INTEGER, name="Oil_Max_Pro")

    # Constraints
    m.addConstr(46*x + 13*y <= Constraint_A, "Constraint_A")
    m.addConstr(43*x + 4*y <= Constraint_B, "Constraint_B")
    m.addConstr(56*x + 45*y <= Constraint_C, "Constraint_C")

    # Objective function
    m.setObjective(10*x + 15*y, GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal)