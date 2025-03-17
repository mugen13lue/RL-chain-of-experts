import gurobipy as gp
from gurobipy import GRB

def prob_275(chemical_A, chemical_B):
    """
    Args:
        chemical_A: an integer representing the amount of chemical A
        chemical_B: an integer representing the amount of chemical B
    Returns:
        obj: an integer representing the total time
    """
    model = gp.Model("chemical_mixer")

    # Variables
    x = model.addVar(lb=300, vtype=GRB.CONTINUOUS, name="chemical_A")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="chemical_B")

    # Constraints
    model.addConstr(x <= 3*y, "chemical_A_limit")
    model.addConstr(x + y >= 1500, "total_chemical_limit")

    # Objective
    model.setObjective(30*x + 45*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return objective value
    return int(model.objVal)