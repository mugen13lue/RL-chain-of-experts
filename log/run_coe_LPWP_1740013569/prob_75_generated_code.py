import gurobipy as gp
from gurobipy import GRB

def prob_75(traditional_machine, modern_machine):
    """
    Args:
        traditional_machine: an integer, represents the number of acres to be used for traditional machine
        modern_machine: an integer, represents the number of acres to be used for modern machine
    Returns:
        obj: an integer, represents the maximum amount of tea leaves that can be picked
    """
    model = gp.Model("Tea Leaves Optimization")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="traditional_machine_acres")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="modern_machine_acres")

    # Constraints
    model.addConstr(30*x + 40*y <= 500, "tea_leaves_constraint")
    model.addConstr(10*x + 15*y <= 6000, "waste_constraint")
    model.addConstr(20*x + 15*y <= 9000, "fuel_constraint")

    # Objective function
    model.setObjective(30*x + 40*y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj