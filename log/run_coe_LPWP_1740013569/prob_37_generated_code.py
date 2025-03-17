from gurobipy import *

def prob_37(mangos, guavas, mango_cost, guava_cost):
    """
    Args:
        mangos: an integer, the number of mangos
        guavas: an integer, the number of guavas
        mango_cost: an integer, the cost of one mango
        guava_cost: an integer, the cost of one guava
    Returns:
        profit: an integer, the maximum profit
    """
    m = Model("food_truck")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="mangos")
    y = m.addVar(vtype=GRB.INTEGER, name="guavas")

    # Constraints
    m.addConstr(5*x + 3*y <= 20000, "budget_constraint")
    m.addConstr(x >= 100, "min_mango_constraint")
    m.addConstr(x <= 150, "max_mango_constraint")
    m.addConstr(y <= (1/3)*x, "guava_constraint")

    # Objective
    m.setObjective(3*x + 4*y, GRB.MAXIMIZE)

    m.optimize()

    return int(m.objVal)