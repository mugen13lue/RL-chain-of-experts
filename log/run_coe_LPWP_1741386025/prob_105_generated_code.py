import gurobipy as gp
from gurobipy import GRB

def prob_105(cleansing_chemical, odor_removing_chemical):
    """
    Args:
        cleansing_chemical: an integer, the units of cleansing chemical used
        odor_removing_chemical: an integer, the units of odor-removing chemical used
    Returns:
        obj: an integer, the total time it takes for a house to be cleaned
    """
    model = gp.Model("house_cleaning")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="cleansing_chemical")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="odor_removing_chemical")

    # Constraints
    model.addConstr(4*x >= 100, "cleansing_chemical_usage")
    model.addConstr(4*x + 6*y <= 300, "total_chemical_usage")
    model.addConstr(x <= 2*y, "ratio_constraint")

    # Objective function
    model.setObjective(4*x + 6*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the total time it takes for a house to be cleaned
    obj = model.objVal

    return obj