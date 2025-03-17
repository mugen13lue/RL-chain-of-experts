import gurobipy as gp
from gurobipy import GRB

def prob_71(top_loading_model, front_loading_model, var1, var2, var3, var4):
    """
    Args:
        top_loading_model: an integer, representing the number of top-loading machines
        front_loading_model: an integer, representing the number of front-loading machines
        var1: an integer, representing the number of items the top-loading model can wash per day
        var2: an integer, representing the number of items the front-loading model can wash per day
        var3: an integer, representing the amount of energy consumed by the top-loading model per day
        var4: an integer, representing the amount of energy consumed by the front-loading model per day
    Returns:
        obj: an integer, representing the minimum total number of washing machines
    """
    m = gp.Model("washing_machine_optimization")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="top_loading_machines")
    y = m.addVar(vtype=GRB.INTEGER, name="front_loading_machines")

    # Constraints
    m.addConstr(x >= 0)
    m.addConstr(y >= 0)
    m.addConstr(x + y >= 10)
    m.addConstr(x <= 0.4 * (x + y))
    m.addConstr(var1 * x + var2 * y >= 5000)
    m.addConstr(var3 * x + var4 * y <= 7000)

    # Objective function
    m.setObjective(x + y, GRB.MINIMIZE)

    # Solve the optimization problem
    m.optimize()

    # Retrieve the optimal objective value
    obj = m.objVal

    return obj