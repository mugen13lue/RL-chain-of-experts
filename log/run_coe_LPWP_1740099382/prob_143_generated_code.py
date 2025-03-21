import gurobipy as gp
from gurobipy import GRB

def prob_143(large_pill, small_pill):
    """
    Args:
        large_pill: an integer representing the number of large pills
        small_pill: an integer representing the number of small pills

    Returns:
        obj: an integer representing the number of filler material needed
    """
    m = gp.Model("pill_optimization")

    # Variables
    x = m.addVar(name="large_pills")
    y = m.addVar(name="small_pills")

    # Constraints
    m.addConstr(3*x + 2*y <= 1000)
    m.addConstr(2*x + y <= 1000)
    m.addConstr(x >= 100)
    m.addConstr(y >= 0.6*(x + y))

    # Objective
    m.setObjective(2*y, GRB.MINIMIZE)

    m.optimize()

    return int(m.objVal)