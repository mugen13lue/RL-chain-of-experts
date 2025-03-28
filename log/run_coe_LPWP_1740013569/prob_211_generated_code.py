import gurobipy as gp
from gurobipy import GRB

def prob_211(laminate_planks, carpets):
    """
    Args:
        laminate_planks: an integer (number of laminate planks produced weekly)
        carpets: an integer (number of carpets produced weekly)

    Returns:
        obj: a float (maximum profit achieved)
    """
    model = gp.Model("flooring_problem")

    # Variables
    x = model.addVar(lb=0, ub=40000, vtype=GRB.INTEGER, name="laminate_planks")
    y = model.addVar(lb=0, ub=20000, vtype=GRB.INTEGER, name="carpets")

    # Constraints
    model.addConstr(x + y >= 50000)
    model.addConstr(x >= 15000)
    model.addConstr(y >= 5000)

    # Objective
    model.setObjective(2.1*x + 3.3*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj