import gurobipy as gp
from gurobipy import GRB

def prob_74(with_a_catalyst, without_a_catalyst):
    """
    Args:
        with_a_catalyst: an integer (number of process with a catalyst),
        without_a_catalyst: an integer (number of process without a catalyst),

    Returns:
        obj: an integer (amount of carbon dioxide produced),
    """
    m = gp.Model("carbon_dioxide_production")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    m.addConstr(10*x + 15*y <= 300, "wood_constraint")
    m.addConstr(20*x + 12*y <= 300, "oxygen_constraint")
    m.addConstr(x >= 0, "non_negativity_x")
    m.addConstr(y >= 0, "non_negativity_y")

    # Objective
    m.setObjective(15*x + 18*y, GRB.MAXIMIZE)

    m.optimize()

    return int(m.objVal)