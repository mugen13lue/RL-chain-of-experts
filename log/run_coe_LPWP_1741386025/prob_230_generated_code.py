from gurobipy import *

def prob_230():
    m = Model("Medication Optimization")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="calcium_pills")
    y = m.addVar(vtype=GRB.INTEGER, name="vitamin_d_pills")

    # Constraints
    m.addConstr(x + y >= 130, "total_pills")
    m.addConstr(y >= 40, "min_vitamin_d")
    m.addConstr(x >= y, "more_calcium_than_vitamin_d")

    # Objective
    m.setObjective(5*x + 6*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    total_time = m.objVal

    return total_time