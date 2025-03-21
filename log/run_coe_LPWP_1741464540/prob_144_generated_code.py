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
    model = gp.Model("pool_optimization")

    # Variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="chlorine")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="water_softener")

    # Constraints
    model.addConstr(x <= 0.5 * y, "chlorine_limit")
    model.addConstr(x >= 200, "min_chlorine")
    model.addConstr(x + y <= 500, "total_chemicals")

    # Objective
    model.setObjective(x + 2*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_time = int(model.objVal)

    return total_time