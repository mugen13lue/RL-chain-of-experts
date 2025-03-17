import gurobipy as gp
from gurobipy import GRB

def prob_62(rural, urban, _100, _8, _200, _20, _260, _3000):
    """
    Args:
        rural: an integer, number of rural factories
        urban: an integer, number of urban factories
        _100: an integer, number of phones that a rural factory can make per day
        _8: an integer, number of managers required for a rural factory
        _200: an integer, number of phones that an urban factory can make per day
        _20: an integer, number of managers required for an urban factory
        _260: an integer, available number of managers
        _3000: an integer, minimum number of phones required per day
    Returns:
        number_of_factories: an integer, total number of factories
    """
    m = gp.Model("factories")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    m.addConstr(8*x + 20*y <= 260, "managers_constraint")
    m.addConstr(100*x + 200*y >= 3000, "phones_constraint")

    # Objective function
    m.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Return total number of factories
    return m.objVal