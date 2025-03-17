import gurobipy as gp
from gurobipy import GRB

def prob_185(labradors, golden_retrievers):
    """
    Args:
        labradors: an integer, the number of labradors used
        golden_retrievers: an integer, the number of golden retrievers used

    Returns:
        obj: an integer, the maximum number of newspapers that can be delivered
    """
    m = gp.Model("newspaper_delivery")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="labradors")
    y = m.addVar(vtype=GRB.INTEGER, name="golden_retrievers")

    # Constraints
    m.addConstr(5*x + 6*y <= 1500)
    m.addConstr(y >= 50)
    m.addConstr(x <= 0.6*(x + y))

    # Objective function
    m.setObjective(7*x + 10*y, sense=GRB.MAXIMIZE)

    # Optimize the model
    m.optimize()

    return int(m.objVal)