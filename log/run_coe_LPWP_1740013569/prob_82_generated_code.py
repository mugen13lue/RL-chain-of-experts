import gurobipy as gp
from gurobipy import GRB

def prob_82(small_shop, large_shop):
    """
    Args:
        small_shop: an integer, the number of small butcher shops
        large_shop: an integer, the number of large butcher shops
        
    Returns:
        number_of_butcher_shops: an integer, the minimum total number of butcher shops
    """
    model = gp.Model("butcher_shop")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(30*x + 70*y >= 500)
    model.addConstr(2*x + 4*y <= 30)
    model.addConstr(x >= 0)
    model.addConstr(y >= 0)

    # Objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    # Return the optimal solution
    return int(x.x + y.x) if model.status == GRB.OPTIMAL else None