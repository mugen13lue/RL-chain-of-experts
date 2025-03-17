import gurobipy as gp
from gurobipy import GRB

def prob_79(peanut_butter_crepes, chocolate_crepes):
    """
    Args:
        peanut_butter_crepes: an integer, the number of peanut butter crepes made
        chocolate_crepes: an integer, the number of chocolate crepes made
    Returns:
        obj: an integer, the total amount of crepe mix needed
    """
    model = gp.Model("crepe_mix_minimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="chocolate_crepes")
    y = model.addVar(vtype=GRB.INTEGER, name="peanut_butter_crepes")

    # Constraints
    model.addConstr(3*x <= 400, "chocolate_spread_constraint")
    model.addConstr(4*y <= 450, "peanut_butter_spread_constraint")
    model.addConstr(6*x + 7*y <= peanut_butter_crepes*7 + chocolate_crepes*6, "crepe_mix_constraint")
    model.addConstr(x >= 0.25*(x+y), "minimum_chocolate_crepe_constraint")
    model.addConstr(y >= x + 1, "peanut_butter_crepe_exceeds_chocolate_crepe_constraint")

    # Objective
    model.setObjective(6*x + 7*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)