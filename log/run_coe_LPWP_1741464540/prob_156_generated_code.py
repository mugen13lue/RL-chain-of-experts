import gurobipy as gp
from gurobipy import GRB

def prob_156(vans, trucks):
    """
    Args:
        vans: an integer, number of vans
        trucks: an integer, number of trucks
        
    Returns:
        obj: an integer, the minimum number of vans that can be used
    """
    model = gp.Model("shoe_transportation")

    # Decision variables
    V = model.addVar(vtype=GRB.INTEGER, name="V")
    T = model.addVar(vtype=GRB.INTEGER, name="T")

    # Constraints
    model.addConstr(V >= 0)
    model.addConstr(T >= 0)
    model.addConstr(V <= T)
    model.addConstr(50*V + 100*T >= 2000)

    # Objective
    model.setObjective(V, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = None
    if model.status == GRB.OPTIMAL:
        obj = model.objVal

    return obj