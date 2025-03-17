import gurobipy as gp
from gurobipy import GRB

def prob_94(chemical_reaction_A, chemical_reaction_B):
    """
    Args:
        chemical_reaction_A: an integer, represents the number of reactions of chemical reaction A
        chemical_reaction_B: an integer, represents the number of reactions of chemical reaction B
    Returns:
        objective: an integer, representing the amount of rare compound produced
    """
    model = gp.Model("chemical_reactions")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(5*x + 7*y <= 1000, "rare_inert_gas")
    model.addConstr(6*x + 3*y <= 800, "treated_water")

    # Objective
    model.setObjective(10*x + 8*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    objective = model.objVal

    return objective