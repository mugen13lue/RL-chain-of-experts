import gurobipy as gp
from gurobipy import GRB

def prob_144(chlorine, water_softener):
    """
    Args:
        chlorine: an integer representing the number of units of chlorine to be added to the pool.
        water_softener: an integer representing the number of units of water softener to be added to the pool.
    Returns:
        total_time: an integer representing the minimum total time it takes for the pool to be ready.
    """
    model = gp.Model("pool_preparation")

    # Variables
    x = model.addVar(lb=200, vtype=GRB.INTEGER, name="chlorine")
    y = model.addVar(lb=0, ub=500, vtype=GRB.INTEGER, name="water_softener")

    # Constraints
    model.addConstr(x + y <= 500, "total_chemical_constraint")
    model.addConstr(x <= 0.5 * y, "ratio_constraint")

    # Objective
    model.setObjective(x + 2*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_time = model.objVal

    return total_time